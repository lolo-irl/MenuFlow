# Arquitetura do Sistema — MenuFlow

**Projeto:** MenuFlow — Cardápio Digital  
**Autor:** Nicolas Costa Boese

## 1. Visão geral

O MenuFlow é uma aplicação web de cardápio digital que permite aos clientes consultar produtos, montar um carrinho e realizar pedidos. Também disponibiliza uma área administrativa para gerenciar produtos e acompanhar pedidos.

A aplicação será desenvolvida utilizando HTML5, CSS3, Bootstrap 5 e JavaScript. Para simular a comunicação com o back-end, será utilizado o JSON Server, que disponibiliza uma API REST baseada em arquivos JSON.

## 2. Arquitetura da aplicação

O sistema será dividido em duas áreas principais:

### 2.1. Área pública

Disponibiliza as funcionalidades utilizadas pelos clientes:

- Visualização do cardápio.
- Pesquisa e filtragem de produtos.
- Consulta de informações, preços e disponibilidade.
- Adição de produtos ao carrinho.
- Alteração de quantidades e remoção de itens.
- Visualização do valor total.
- Identificação do cliente por nome e telefone.
- Seleção entre retirada e consumo no estabelecimento.
- Finalização do pedido.

### 2.2. Área administrativa

Disponibiliza as funcionalidades utilizadas pelo administrador:

- Acesso por uma tela de login demonstrativa.
- Visualização de indicadores gerais no dashboard.
- Cadastro, edição e exclusão de produtos.
- Controle de disponibilidade dos produtos.
- Listagem e visualização dos pedidos.
- Atualização do status dos pedidos.

## 3. Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização |
| Bootstrap 5 | Componentes e responsividade |
| JavaScript | Lógica e interatividade |
| jQuery | Manipulação do DOM e integração com plugins |
| jQuery Mask Plugin | Máscara para campos de telefone |
| JSON Server | Simulação de uma API REST |
| Fetch API | Comunicação assíncrona com a API |
| localStorage | Persistência local do carrinho |
| Node.js e NPM | Gerenciamento do ambiente e dependências |
| Sass | Organização e compilação dos estilos |
| ESLint | Padronização e análise do código JavaScript |
| Prettier | Formatação do código |

## 4. Modelo de dados

O sistema utilizará quatro entidades principais: CLIENTE, PRODUTO, PEDIDO e ITEM_PEDIDO.

A entidade ITEM_PEDIDO será responsável por relacionar os pedidos aos produtos, armazenando a quantidade e o preço registrado no momento da compra.

### 4.1. Diagrama entidade-relacionamento

```mermaid
erDiagram
    CLIENTE ||--o{ PEDIDO : realiza
    PEDIDO ||--|{ ITEM_PEDIDO : possui
    PRODUTO ||--o{ ITEM_PEDIDO : compoe

    CLIENTE {
        int id PK
        string nome
        string telefone
    }

    PRODUTO {
        int id PK
        string nome
        string descricao
        decimal preco
        string imagem
        string categoria
        boolean disponivel
    }

    PEDIDO {
        int id PK
        int cliente_id FK
        string modalidade
        string observacao
        decimal valor_total
        string status
        datetime data_criacao
    }

    ITEM_PEDIDO {
        int id PK
        int pedido_id FK
        int produto_id FK
        int quantidade
        decimal preco_unitario
    }
````

### 4.2. Descrição das entidades

CLIENTE

Armazena os dados de identificação dos clientes.

- `id`: identificador único.
- `nome`: nome informado pelo cliente.
- `telefone`: telefone utilizado para identificação.

PRODUTO

Armazena os produtos disponíveis no cardápio.

- `id`: identificador único.
- `nome`: nome do produto.
- `descricao`: descrição do produto.
- `preco`: preço atual.
- `imagem`: caminho ou endereço da imagem.
- `categoria`: categoria do produto.
- `disponivel`: indica se o produto pode ser solicitado.

PEDIDO

Armazena as informações gerais de cada pedido.

- `id`: identificador único.
- `cliente_id`: referência ao cliente responsável.
- `modalidade`: retirada ou consumo no estabelecimento.
- `observacao`: informação adicional opcional.
- `valor_total`: valor total do pedido.
- `status`: situação atual do pedido.
- `data_criacao`: data e horário de criação.

ITEM_PEDIDO

Relaciona os produtos aos pedidos.

- `id`: identificador único.
- `pedido_id`: referência ao pedido.
- `produto_id`: referência ao produto.
- `quantidade`: quantidade solicitada.
- `preco_unitario`: preço do produto no momento da compra.

## 5. Relacionamentos

- Um cliente pode realizar vários pedidos, mas cada pedido pertence a um único cliente.
- Um pedido possui um ou mais itens.
- Um produto pode estar presente em vários itens de pedidos diferentes.
- A entidade ITEM_PEDIDO permite relacionar pedidos e produtos, além de registrar a quantidade e o preço praticado no momento da compra.

## 6. Estrutura da API

O JSON Server será utilizado para disponibilizar os dados por meio de endpoints REST.

### 6.1. Endpoints planejados

| Método | Endpoint        | Descrição                    |
| ------ | --------------- | ---------------------------- |
| GET    | `/produtos`     | Listar produtos              |
| GET    | `/produtos/:id` | Consultar produto específico |
| POST   | `/produtos`     | Cadastrar produto            |
| PUT    | `/produtos/:id` | Atualizar produto            |
| DELETE | `/produtos/:id` | Excluir produto              |
| GET    | `/clientes`     | Listar clientes              |
| POST   | `/clientes`     | Cadastrar cliente            |
| GET    | `/pedidos`      | Listar pedidos               |
| GET    | `/pedidos/:id`  | Consultar pedido específico  |
| POST   | `/pedidos`      | Criar pedido                 |
| PATCH  | `/pedidos/:id`  | Atualizar status do pedido   |
| GET    | `/itensPedido`  | Listar itens dos pedidos     |
| POST   | `/itensPedido`  | Cadastrar item de pedido     |

### 6.2. Estrutura do arquivo db.json

Os dados serão organizados em coleções dentro do arquivo `db.json`.

Exemplo simplificado:

```
{
  "clientes": [],
  "produtos": [],
  "pedidos": [],
  "itensPedido": []
}
```

## 7. Comunicação entre front-end e API

A comunicação será realizada por meio da Fetch API, utilizando funções assíncronas com `async` e `await`.

As operações de consulta, cadastro, atualização e exclusão serão realizadas por requisições HTTP.

Exemplo de consulta:

```
async function buscarProdutos() {
    try {
        const resposta = await fetch("http://localhost:3000/produtos");

        if (!resposta.ok) {
            throw new Error("Erro ao buscar produtos.");
        }

        const produtos = await resposta.json();

        return produtos;
    } catch (erro) {
        console.error(erro);
        return [];
    }
}
```

## 8. Persistência de dados

O sistema utilizará duas formas de armazenamento:

### 8.1. JSON Server

Será responsável por armazenar os dados principais da aplicação:

- Clientes.
- Produtos.
- Pedidos.
- Itens dos pedidos.

### 8.2. localStorage

Será utilizado para armazenar temporariamente o carrinho de compras no navegador.

Dessa forma, os itens adicionados permanecerão no carrinho mesmo após o usuário atualizar ou fechar a página.

O carrinho será removido do `localStorage` após a finalização bem-sucedida do pedido.

## 9. Fluxos principais

### 9.1. Cadastro e gerenciamento de produtos

1. O administrador acessa a área administrativa.
2. Abre a página de gerenciamento de produtos.
3. Cadastra, edita ou exclui produtos.
4. As alterações são enviadas à API.
5. O cardápio público consulta os dados atualizados.

### 9.2. Adição de produtos ao carrinho

1. O cliente acessa o cardápio.
2. Seleciona os produtos desejados.
3. Adiciona os produtos ao carrinho.
4. O sistema atualiza as quantidades e o valor total.
5. Os dados do carrinho são armazenados no `localStorage`.

### 9.3. Finalização do pedido

1. O cliente acessa a página de finalização.
2. Informa nome e telefone.
3. Seleciona a modalidade do pedido.
4. Adiciona uma observação, caso necessário.
5. O sistema verifica se o cliente já está cadastrado pelo telefone.
6. Caso não exista, realiza o cadastro do cliente.
7. Cria o pedido na API.
8. Registra os produtos e suas respectivas quantidades na coleção `itensPedido`.
9. Limpa o carrinho após a confirmação das operações.
10. Exibe uma mensagem de confirmação ao cliente.

### 9.4. Gerenciamento de pedidos

1. O administrador acessa a página de pedidos.
2. O sistema consulta os pedidos registrados na API.
3. O administrador visualiza os detalhes de cada pedido.
4. Atualiza o status conforme o andamento.
5. A API registra a alteração.

Os status previstos são:

- Pendente.
- Em preparo.
- Concluído.

## 10. Validações e regras de negócio

- O nome e o telefone do cliente são obrigatórios para finalizar um pedido.
- O telefone será utilizado como critério de identificação do cliente.
- Não será permitido adicionar produtos indisponíveis ao carrinho.
- A quantidade de cada item deverá ser maior que zero.
- O valor total será calculado com base nos preços e quantidades dos itens.
- O preço unitário deverá ser registrado no ITEM_PEDIDO para preservar o valor praticado no momento da compra.
- Um pedido deverá possuir pelo menos um item.
- O carrinho somente será limpo após a confirmação da criação do pedido e de seus itens.
- O administrador poderá alterar o status dos pedidos.

## 11. Estrutura de diretórios planejada

```
menuflow/
│
├── admin/
│   ├── login.html
│   ├── dashboard.html
│   ├── produtos.html
│   └── pedidos.html
│
├── assets/
│   ├── css/
│   ├── js/
│   └── images/
│
├── docs/
│   ├── prd.md
│   └── architecture.md
│
├── index.html
├── cardapio.html
├── finalizar-pedido.html
│
├── db.json
├── package.json
└── README.md
```

## 12. Considerações técnicas e limitações

O JSON Server será utilizado para fins acadêmicos e de demonstração. Ele permite simular operações de uma API REST, mas não oferece os mesmos recursos de segurança e controle de um back-end de produção.

O login administrativo será demonstrativo e não deverá ser considerado um mecanismo seguro de autenticação.

Caso o projeto seja publicado no GitHub Pages, será necessário hospedar a API JSON Server separadamente, pois o GitHub Pages disponibiliza apenas arquivos estáticos.

Para uma aplicação real, seria necessário implementar um back-end próprio, autenticação segura, autorização de usuários e validações no servidor.

```
```