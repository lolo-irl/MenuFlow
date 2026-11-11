# 📄 Product Requirements Document (PRD)

## 1. Identificação

| Campo                 | Informação                                                           |
| --------------------- | -------------------------------------------------------------------- |
| **Projeto**           | MenuFlow — Cardápio Digital                                          |
| **Autor**             | Nicolas Boese                                                        |
| **Tema**              | Sistema web para visualização de cardápio e gerenciamento de pedidos |
| **Tipo de aplicação** | Front-end web com API fake (JSON Server)                             |

## 2. Descrição do Projeto

O MenuFlow é uma aplicação web que permite a um estabelecimento organizar e disponibilizar seu cardápio digital, além de registrar e acompanhar pedidos realizados pelos clientes.

O sistema possui duas áreas principais: uma área administrativa, destinada ao gerenciamento dos produtos e dos pedidos, e uma área pública, na qual os clientes consultam o cardápio, montam seus carrinhos e finalizam pedidos.

O projeto busca centralizar as informações do cardápio e dos pedidos em uma API, evitando que os dados precisem ser inseridos diretamente nas páginas. A aplicação também utiliza Web Storage para preservar temporariamente o carrinho do cliente durante a navegação.

## 3. Problema e Justificativa

Estabelecimentos que disponibilizam seus produtos apenas por meios informais, como imagens, mensagens ou cardápios estáticos, podem ter dificuldade para manter preços e disponibilidade atualizados e organizar os pedidos recebidos.

O MenuFlow propõe uma interface simples para consultar produtos e registrar pedidos, enquanto oferece ao administrador uma área para manter o cardápio atualizado e acompanhar os pedidos recebidos.

O projeto também permite aplicar, em um cenário prático, conceitos de desenvolvimento front-end, responsividade, validação de formulários, armazenamento local e consumo de uma API REST simulada.

## 4. Objetivos

### 4.1 Objetivo geral

Desenvolver uma aplicação web responsiva para consulta de cardápio, registro de pedidos e gerenciamento administrativo de produtos e pedidos.

### 4.2 Objetivos específicos

- Disponibilizar os produtos cadastrados em um cardápio digital.
- Permitir que o administrador cadastre, edite, consulte e remova produtos.
- Permitir que clientes montem um carrinho e enviem pedidos.
- Identificar os pedidos por meio dos dados informados pelo cliente.
- Permitir que o administrador consulte os pedidos e atualize seus status.
- Persistir produtos, clientes e pedidos por meio do JSON Server.
- Utilizar Web Storage para preservar o carrinho no navegador.
- Desenvolver interfaces adaptáveis a dispositivos móveis e desktops.

## 5. Atores do Sistema

### 5.1 Visitante / Cliente

Pessoa que acessa a área pública para consultar o cardápio e realizar pedidos. Não será necessário criar uma conta ou efetuar login. Para concluir um pedido, o cliente informará seu nome e telefone.

### 5.2 Administrador

Responsável pela manutenção do cardápio e pelo acompanhamento dos pedidos. A área administrativa será acessada por uma tela de login demonstrativa, com credenciais previamente definidas no projeto.

**Limitação do protótipo:** como a aplicação utiliza front-end e JSON Server, sem um backend com autenticação e autorização, o login administrativo terá finalidade demonstrativa. Ele não representa um mecanismo seguro para proteger dados em produção.

## 6. Histórias de Usuário e Escopo Funcional

As histórias abaixo representam o escopo planejado para a aplicação.

### 6.1 Acesso e navegação

- [x] **US01 — Acesso ao cardápio:** Como visitante, quero acessar o cardápio digital para visualizar os produtos disponíveis no estabelecimento.
- [ ] **US02 — Acesso administrativo:** Como administrador, quero acessar uma área administrativa por meio de uma tela de login para utilizar as funcionalidades de gerenciamento. _(interface pronta na Atividade 08; lógica pendente)_
- [x] **US03 — Navegação responsiva:** Como usuário, quero utilizar o sistema em dispositivos móveis e desktops para acessar suas funcionalidades em diferentes tamanhos de tela.

### 6.2 Gerenciamento de produtos

- [ ] **US04 — Cadastro de produto:** Como administrador, quero cadastrar um produto informando nome, descrição, categoria, preço e imagem para disponibilizá-lo no cardápio. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US05 — Listagem de produtos:** Como administrador, quero visualizar os produtos cadastrados em uma listagem para consultar o cardápio gerenciado. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US06 — Edição de produto:** Como administrador, quero editar as informações de um produto para manter seus dados atualizados. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US07 — Exclusão de produto:** Como administrador, quero remover um produto para retirar do sistema itens que não serão mais oferecidos. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US08 — Disponibilidade:** Como administrador, quero marcar um produto como disponível ou indisponível para controlar sua exibição e possibilidade de pedido. _(interface pronta na Atividade 08; lógica pendente)_

### 6.3 Consulta do cardápio e carrinho

- [ ] **US09 — Visualização de produtos:** Como cliente, quero visualizar os produtos com nome, descrição, imagem e preço para escolher o que desejo pedir. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US10 — Busca e categorias:** Como cliente, quero pesquisar produtos e filtrar por categoria para encontrar itens com mais facilidade. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US11 — Adicionar ao carrinho:** Como cliente, quero adicionar produtos ao carrinho para reunir os itens que desejo solicitar. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US12 — Alterar carrinho:** Como cliente, quero alterar quantidades ou remover itens do carrinho para ajustar meu pedido. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US13 — Persistência do carrinho:** Como cliente, quero que os itens do carrinho permaneçam salvos durante a navegação e após atualizar a página para não perder meu pedido.
- [ ] **US14 — Visualizar total:** Como cliente, quero visualizar o valor total do carrinho para saber quanto custará meu pedido antes de finalizá-lo. _(interface pronta na Atividade 08; lógica pendente)_

### 6.4 Identificação e registro de pedidos

- [ ] **US15 — Informar dados do cliente:** Como cliente, quero informar meu nome e telefone ao finalizar o pedido para que o estabelecimento saiba quem realizou a solicitação. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US16 — Informar modalidade:** Como cliente, quero selecionar a modalidade do pedido (retirada no local ou consumo no estabelecimento) para indicar como pretendo receber ou consumir os itens. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US17 — Adicionar observação:** Como cliente, quero incluir uma observação opcional para informar detalhes relevantes sobre meu pedido. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US18 — Finalizar pedido:** Como cliente, quero confirmar meu carrinho e enviar o pedido para que o estabelecimento possa recebê-lo e prepará-lo. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US19 — Confirmação:** Como cliente, quero receber uma confirmação visual após o envio para saber que meu pedido foi registrado. _(interface pronta na Atividade 08; lógica pendente)_

### 6.5 Administração de pedidos

- [ ] **US20 — Consultar pedidos:** Como administrador, quero visualizar os pedidos recebidos com identificação do cliente, itens, valor, data e status para acompanhar as solicitações. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US21 — Consultar detalhes:** Como administrador, quero visualizar os detalhes de um pedido para conferir os produtos e as observações informadas. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US22 — Atualizar status:** Como administrador, quero alterar o status de um pedido para informar se está pendente, em preparo ou concluído. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US23 — Resumo administrativo:** Como administrador, quero visualizar indicadores simples, como quantidade de produtos e pedidos pendentes, para acompanhar o funcionamento do sistema. _(interface pronta na Atividade 08; lógica pendente)_
- [ ] **US24 — Consulta de informações nutricionais:** Como administrador, quero consultar informações nutricionais e ingredientes de produtos industrializados por meio do código de barras, para complementar os dados apresentados aos clientes.

## 7. Regras de Negócio

1. Somente produtos marcados como disponíveis poderão ser adicionados ao carrinho.
2. O preço considerado no pedido deverá ser registrado no momento da finalização, para preservar o valor praticado naquela compra.
3. Um pedido deverá possuir ao menos um item.
4. O nome e o telefone do cliente serão obrigatórios para finalizar um pedido.
5. A modalidade do pedido deverá ser selecionada entre retirada no local e consumo no estabelecimento.
6. A observação do pedido será opcional.
7. O total do pedido será calculado pela soma dos preços dos itens multiplicados por suas quantidades.
8. Cada pedido deverá estar associado a um cadastro de cliente.
9. Os status previstos para os pedidos serão: **Pendente**, **Em preparo** e **Concluído**.
10. O administrador poderá alterar a disponibilidade dos produtos e o status dos pedidos.
11. O carrinho será armazenado no navegador por meio do `localStorage`; os produtos, clientes e pedidos serão persistidos no JSON Server.
12. A consulta à API Open Food Facts será opcional. Os dados retornados poderão complementar as informações dos produtos, mas não substituirão os dados cadastrados pelo administrador.
13. Caso o produto não seja encontrado na API externa, o cadastro deverá continuar funcionando normalmente.

## 8. Fora do Escopo

Para manter o projeto compatível com os objetivos acadêmicos e com o escopo mínimo da disciplina, não serão implementados inicialmente:

- Pagamento on-line ou integração com meios de pagamento.
- Entrega com rastreamento ou cálculo de frete.
- Autenticação real, cadastro de contas e recuperação de senha.
- Controle de estoque por quantidade.
- Impressão ou envio automático de pedidos por WhatsApp.
- Integração com sistemas reais de restaurantes.
- Aplicativo nativo para dispositivos móveis.

## 9. Requisitos Não Funcionais

- **RNF01 — Responsividade:** as páginas deverão se adaptar a telas mobile e desktop.
- **RNF02 — Usabilidade:** a navegação deverá ser simples e apresentar mensagens claras de validação, erro e sucesso.
- **RNF03 — Consistência visual:** a aplicação deverá seguir um Design System com cores, tipografia, espaçamentos e componentes padronizados.
- **RNF04 — Organização:** HTML, CSS/SCSS e JavaScript deverão ser organizados em arquivos e módulos separados.
- **RNF05 — Persistência:** os dados de produtos, clientes e pedidos deverão ser manipulados por meio da API JSON Server; o carrinho deverá utilizar Web Storage.
- **RNF06 — Compatibilidade:** a aplicação deverá funcionar em navegadores modernos.
- **RNF07 — Acessibilidade básica:** formulários deverão possuir rótulos, campos identificáveis e mensagens compreensíveis.

## 10. Critérios de Aceitação

O projeto será considerado funcional quando:

- [x] Existirem ao menos três páginas HTML distintas e responsivas.
- [ ] O administrador conseguir cadastrar e consultar produtos por meio da API.
- [ ] O cliente conseguir consultar os produtos disponibilizados pela API.
- [ ] O carrinho utilizar Web Storage para preservar os itens.
- [ ] O cliente conseguir enviar um pedido com nome, telefone, modalidade e ao menos um produto.
- [ ] O pedido for persistido na API e aparecer na área administrativa com os dados do cliente.
- [ ] O administrador conseguir consultar os detalhes e atualizar o status do pedido.
- [ ] Os formulários possuírem campos obrigatórios e validação no lado cliente.
