# MenuFlow — Cardápio Digital

### Autor: Nicolas Boese

O **MenuFlow** é uma aplicação web de cardápio digital e gerenciamento de pedidos. O sistema possui uma área pública, na qual os clientes consultam produtos, montam um carrinho e registram pedidos, e uma área administrativa, destinada ao gerenciamento de produtos e ao acompanhamento dos pedidos.

A aplicação utiliza uma API fake com JSON Server para persistir produtos, clientes, pedidos e itens de pedidos. O carrinho do cliente é mantido localmente por meio do Web Storage (`localStorage`).

## 📚 Documentação do Projeto

- [📄 Product Requirements Document (PRD)](docs/prd.md) — propósito, atores, regras de negócio e histórias de usuário.
- [🛠️ Especificação Técnica (Architecture)](docs/architecture.md) — arquitetura, modelo de dados, relacionamentos, rotas da API e fluxos principais.

## 🎨 Design

- **Prototipação no Figma:** https://stitch.google.com/projects/5892625441821988342.

## 🌐 Site em Produção

- **GitHub Pages:** `A definir — inserir aqui a URL após publicar o projeto`.

> O GitHub Pages hospeda apenas o front-end estático. Para que as operações de consulta e gravação funcionem na versão publicada, a API JSON Server deverá estar hospedada separadamente e a URL da API deverá ser configurada no projeto.

## 💻 Tecnologias e Dependências

### Framework CSS

- **Bootstrap 5** — grid responsivo, componentes de interface, formulários e elementos de navegação.

### Tecnologias principais

- HTML5
- CSS3 / SCSS
- JavaScript
- JSON Server — API REST fake.
- Fetch API — requisições assíncronas.
- Web Storage (`localStorage`) — persistência local do carrinho.
- Node.js e NPM — ambiente e gerenciamento de dependências.

### Bibliotecas e ferramentas JavaScript previstas

- **jQuery** — manipulação do DOM e eventos.
- **jQuery Mask Plugin** — máscara do campo de telefone.
- **JSON Server** — simulação da API REST.
- **Sass** — compilação dos estilos SCSS.
- **ESLint** — análise estática do JavaScript.
- **Prettier** — formatação de código.

> As dependências e respectivas versões serão registradas no `package.json` durante a configuração do projeto.

## ✅ Checklist | Funcionalidades

Os itens abaixo representam os indicadores de desempenho da disciplina. As caixas deverão ser marcadas conforme cada funcionalidade for efetivamente implementada e testada.

### RA1 — Frameworks CSS, layouts e responsividade

- [ ] **ID 01** — Prototipa interfaces adaptáveis para mobile e desktop no Figma ou ferramenta equivalente.
- [ ] **ID 02** — Implementa layout responsivo com Bootstrap, utilizando Flexbox ou Grid do framework.
- [ ] **ID 03** — Implementa layout responsivo com CSS próprio, utilizando Flexbox ou Grid Layout.
- [ ] **ID 04** — Utiliza componentes do Bootstrap e componentes JavaScript do framework.
- [ ] **ID 05** — Utiliza unidades relativas (`vw`, `vh`, `%`, `em`, `rem`) para criar layouts fluidos.
- [ ] **ID 06** — Aplica um Design System consistente em toda a aplicação.
- [ ] **ID 07** — Utiliza Sass/SCSS com variáveis, mixins e funções.
- [ ] **ID 08** — Implementa tipografia responsiva com media queries mobile first ou `clamp()`.
- [ ] **ID 09** — Aplica técnicas de responsividade de imagens, como `object-fit` e containers fluidos.
- [ ] **ID 10** — Otimiza imagens com formatos modernos, como WebP, e carregamento adaptativo.

### RA2 — Formulários, validações e Web Storage

- [ ] **ID 11** — Implementa validação HTML nativa, campos obrigatórios e mensagens de erro/sucesso.
- [ ] **ID 12** — Aplica expressões regulares (REGEX) para validações customizadas, como telefone.
- [ ] **ID 13** — Utiliza elementos de seleção, como checkbox, radio e select.
- [ ] **ID 14** — Implementa leitura e escrita no Web Storage (`localStorage` ou `sessionStorage`).

### RA3 — Ferramentas e organização do desenvolvimento

- [x] **ID 15** — Configura o ambiente com Node.js e NPM.
- [x] **ID 16** — Utiliza Git/GitHub com organização de branches e arquivo `.gitignore`.
- [x] **ID 17** — Mantém este README padronizado e atualiza o checklist durante o desenvolvimento.
- [ ] **ID 18** — Organiza os arquivos de forma modular.
- [ ] **ID 19** — Configura ESLint e Prettier.

### RA4 — Bibliotecas JavaScript e interatividade

- [ ] **ID 20** — Utiliza jQuery para manipulação do DOM e interatividade.
- [ ] **ID 21** — Integra um plugin jQuery relevante, como jQuery Mask Plugin.

### RA5 — Requisições assíncronas e APIs

- [ ] **ID 22** — Realiza requisições assíncronas para a API fake para persistir dados de formulários.
- [ ] **ID 23** — Realiza requisições assíncronas para a API fake para exibir dados nas páginas.
- [ ] **ID 24** — Integra uma API pública real, tratando respostas e erros. `Opcional / a definir conforme orientação da disciplina`.

## 🚀 Manual de Execução

### 1. Pré-requisitos

Instale os seguintes programas:

- [Node.js](https://nodejs.org/) (inclui NPM).
- [Git](https://git-scm.com/).
- Um editor de código, como [Visual Studio Code](https://code.visualstudio.com/).

### 2. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
cd menuflow
```

Substitua `URL_DO_REPOSITORIO` pela URL do repositório criado no GitHub.

### 3. Instalar as dependências

```bash
npm install
```

### 4. Iniciar a API JSON Server

O comando será definido no `package.json`. A execução prevista é:

```bash
npm run api
```

A API deverá ficar disponível em:

```text
http://localhost:3000
```

As rotas principais serão:

- `http://localhost:3000/produtos`
- `http://localhost:3000/clientes`
- `http://localhost:3000/pedidos`
- `http://localhost:3000/itensPedido`

### 5. Executar o front-end

Com a API em execução, abra o projeto no Visual Studio Code e utilize a extensão Live Server para iniciar as páginas HTML.

> O front-end e o JSON Server precisam estar em execução ao mesmo tempo para que as operações de consulta e persistência funcionem localmente.

## 📱 Telas da Aplicação

As imagens abaixo deverão ser adicionadas após a implementação das telas. Sugestão de capturas:

1. Página inicial e cardápio público.
2. Carrinho e formulário de finalização do pedido.
3. Dashboard administrativo.
4. Gerenciamento de produtos.
5. Listagem e detalhes dos pedidos.

**Capturas de tela:** adicionar as imagens em `docs/screenshots/` e referenciá-las aqui, por exemplo:

```markdown
![Cardápio digital](docs/screenshots/cardapio.png)
![Dashboard administrativo](docs/screenshots/dashboard.png)
```

## 📌 Escopo do Projeto

O escopo inicial contempla:

- Consulta de produtos disponíveis no cardápio.
- Pesquisa e filtro por categoria.
- Carrinho com persistência em `localStorage`.
- Identificação do cliente por nome e telefone na finalização.
- Registro de pedidos por meio da API JSON Server.
- Cadastro, edição, exclusão e controle de disponibilidade de produtos.
- Consulta de pedidos e atualização de status na área administrativa.

Não fazem parte da primeira versão pagamentos on-line, entrega com rastreamento ou autenticação real de usuários.
