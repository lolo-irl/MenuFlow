import json, pathlib, re, subprocess, sys

raiz = pathlib.Path(".")
assert (raiz / "styles" / "styles.css").exists(), "rode na raiz do MenuFlow (styles/styles.css nao encontrado)"
assert not (raiz / "assets" / "scss").exists(), "assets/scss ja existe; confira antes de rodar"
assert (raiz / "node_modules" / "sass").exists(), "rode antes: npm install --save-dev sass"

FILES = {}

FILES["assets/scss/_variables.scss"] = """// ==== CORES ====
// Cor principal do MenuFlow (terracota): botões, links e destaques.
$cor-primaria: #a43700;
$cor-primaria-escura: #852d00; // hover e estados ativos
$cor-primaria-clara: #ffeedf; // fundos suaves (bg-primary-subtle)
$cor-primaria-foco: #d28a66; // borda de campos em foco
$cor-primaria-gradiente: #cd4700; // fim do degradê do banner
$cor-primaria-rgb: 164, 55, 0; // mesma cor em RGB (usada nas variáveis --bs-*-rgb)
$cor-primaria-escura-rgb: 133, 45, 0;

// Cor secundária (verde culinário): disponibilidade e sucesso.
$cor-sucesso: #1b6d24;
$cor-sucesso-clara: #e2f5e4;
$cor-sucesso-rgb: 27, 109, 36;

// Cores de página
$cor-fundo: #f9f9fc;
$cor-texto: #111c2d;

// ==== TIPOGRAFIA ====
$espacamento-letras: 0.05em; // rótulos em caixa alta

// ==== ESPAÇAMENTO E EFEITOS ====
// Compensa a navbar sticky ao navegar por âncoras.
$compensacao-ancora: 5rem;
// Anel de foco dos campos de formulário.
$foco-espessura: 0.25rem;
$foco-opacidade: 0.25;
"""

FILES["assets/scss/_mixins.scss"] = """@use 'variables';

// Anel de foco padrão do tema, reutilizado por campos e radios.
@mixin foco-anel {
  box-shadow: 0 0 0 variables.$foco-espessura
    rgba(variables.$cor-primaria, variables.$foco-opacidade);
}

// Campo marcado ou em foco: mesma borda e mesmo anel, em um só lugar.
@mixin foco-campo {
  border-color: variables.$cor-primaria-foco;
  @include foco-anel;
}
"""

FILES["assets/scss/_base.scss"] = """@use 'variables';

// Tema: sobrescreve as variáveis CSS do Bootstrap 5.3 (--bs-*), sem !important.
:root {
  --bs-primary: #{variables.$cor-primaria};
  --bs-primary-rgb: #{variables.$cor-primaria-rgb};
  --bs-primary-bg-subtle: #{variables.$cor-primaria-clara};
  --bs-primary-text-emphasis: #{variables.$cor-primaria-escura};

  --bs-success: #{variables.$cor-sucesso};
  --bs-success-rgb: #{variables.$cor-sucesso-rgb};
  --bs-success-bg-subtle: #{variables.$cor-sucesso-clara};
  --bs-success-text-emphasis: #{variables.$cor-sucesso};

  --bs-body-bg: #{variables.$cor-fundo};
  --bs-body-color: #{variables.$cor-texto};

  --bs-link-color: #{variables.$cor-primaria};
  --bs-link-color-rgb: #{variables.$cor-primaria-rgb};
  --bs-link-hover-color: #{variables.$cor-primaria-escura};
  --bs-link-hover-color-rgb: #{variables.$cor-primaria-escura-rgb};
}

// Evita que a navbar sticky cubra o título ao clicar em âncoras (#como-funciona)
html {
  scroll-padding-top: variables.$compensacao-ancora;
}

// Tipografia
.letter-spacing-1 {
  letter-spacing: variables.$espacamento-letras;
}
"""

FILES["assets/scss/_components.scss"] = """@use 'variables';
@use 'mixins';

// Botões: o Bootstrap compila essas cores fixas, então redefinimos as variáveis do componente.
.btn-primary {
  --bs-btn-bg: #{variables.$cor-primaria};
  --bs-btn-border-color: #{variables.$cor-primaria};
  --bs-btn-hover-bg: #{variables.$cor-primaria-escura};
  --bs-btn-hover-border-color: #{variables.$cor-primaria-escura};
  --bs-btn-active-bg: #{variables.$cor-primaria-escura};
  --bs-btn-active-border-color: #{variables.$cor-primaria-escura};
  --bs-btn-disabled-bg: #{variables.$cor-primaria};
  --bs-btn-disabled-border-color: #{variables.$cor-primaria};
  --bs-btn-focus-shadow-rgb: #{variables.$cor-primaria-rgb};
}

.btn-outline-primary {
  --bs-btn-color: #{variables.$cor-primaria};
  --bs-btn-border-color: #{variables.$cor-primaria};
  --bs-btn-hover-bg: #{variables.$cor-primaria};
  --bs-btn-hover-border-color: #{variables.$cor-primaria};
  --bs-btn-active-bg: #{variables.$cor-primaria};
  --bs-btn-active-border-color: #{variables.$cor-primaria};
  --bs-btn-disabled-color: #{variables.$cor-primaria};
  --bs-btn-disabled-border-color: #{variables.$cor-primaria};
  --bs-btn-focus-shadow-rgb: #{variables.$cor-primaria-rgb};
}

// Categorias do cardápio
.nav-pills {
  --bs-nav-pills-link-active-bg: #{variables.$cor-primaria};
}

// Formulários: aninhamento dos estados (:focus, :checked) e uso do mixin.
.form-control,
.form-select {
  &:focus {
    @include mixins.foco-campo;
  }
}

.form-check-input {
  &:checked {
    background-color: variables.$cor-primaria;
    border-color: variables.$cor-primaria;
  }

  &:focus {
    @include mixins.foco-campo;
  }
}
"""

FILES["assets/scss/_layout.scss"] = """@use 'variables';

// Banner de chamada para ação (seção da página inicial)
.card-banner-cta {
  background: linear-gradient(
    135deg,
    variables.$cor-primaria 0%,
    variables.$cor-primaria-gradiente 100%
  );
}
"""

FILES["assets/scss/main.scss"] = """// Arquivo principal: importa os módulos com @use.
// Compilado para assets/css/style.css (npm run sass).

@use 'variables';
@use 'mixins';
@use 'base';
@use 'components';
@use 'layout';
"""

for caminho, conteudo in FILES.items():
    p = raiz / caminho
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(conteudo, encoding="utf-8")
    print("criado:", caminho)

# --- package.json: scripts do Sass
pj = raiz / "package.json"
dados = json.loads(pj.read_text(encoding="utf-8"))
dados.setdefault("scripts", {})
dados["scripts"]["sass"] = "sass assets/scss/main.scss assets/css/style.css --style=expanded --no-source-map"
dados["scripts"]["sass:watch"] = "sass --watch assets/scss/main.scss:assets/css/style.css --style=expanded --no-source-map"
pj.write_text(json.dumps(dados, indent=4, ensure_ascii=False) + "\n", encoding="utf-8")
print("atualizado: package.json (scripts sass e sass:watch)")

# --- .prettierignore: o CSS gerado nao deve ser reformatado
pi = raiz / ".prettierignore"
atual = pi.read_text(encoding="utf-8") if pi.exists() else ""
if "assets/css/" not in atual:
    pi.write_text(atual + ("" if atual.endswith("\n") or not atual else "\n") + "assets/css/\n", encoding="utf-8")
    print("atualizado: .prettierignore")

# --- compilar
(raiz / "assets" / "css").mkdir(parents=True, exist_ok=True)
r = subprocess.run(["npm", "run", "sass"], capture_output=True, text=True)
print(r.stdout + r.stderr)
assert r.returncode == 0, "a compilacao do Sass falhou; nenhuma pagina foi alterada"
assert (raiz / "assets" / "css" / "style.css").exists(), "style.css nao foi gerado"

# --- trocar o link nas paginas
trocadas = []
for html in list(raiz.glob("*.html")) + list(raiz.glob("pages/**/*.html")):
    t = html.read_text(encoding="utf-8")
    if "styles/styles.css" in t:
        html.write_text(t.replace("styles/styles.css", "assets/css/style.css"), encoding="utf-8")
        trocadas.append(str(html))
print("paginas atualizadas (%d):" % len(trocadas))
for h in sorted(trocadas):
    print("  ", h)

# --- docs/architecture.md
arq = raiz / "docs" / "architecture.md"
if arq.exists():
    t = arq.read_text(encoding="utf-8")
    secao11 = """## 11. Estrutura de diretórios

Estrutura adotada a partir da Atividade 08 e ampliada na atividade de Sass. Itens marcados como _(planejado)_ ainda não existem no projeto.

```
MenuFlow/
│
├── index.html                    # página inicial (na raiz)
│
├── pages/
│   ├── client/                   # área pública
│   │   ├── cardapio.html
│   │   └── finalizar-pedido.html
│   └── admin/                    # área administrativa
│       ├── login.html
│       ├── dashboard.html
│       ├── produtos.html
│       └── pedidos.html
│
├── assets/
│   ├── scss/                     # código-fonte dos estilos (Sass)
│   │   ├── _variables.scss
│   │   ├── _mixins.scss
│   │   ├── _base.scss
│   │   ├── _components.scss
│   │   ├── _layout.scss
│   │   └── main.scss
│   ├── css/
│   │   └── style.css             # gerado pelo Sass (versionado)
│   ├── js/                       # (planejado)
│   └── images/                   # (planejado)
│
├── docs/
│   ├── prd.md
│   └── architecture.md
│
├── db.json                       # (planejado)
├── package.json
├── .prettierrc
├── .prettierignore
└── README.md
```

O CSS do projeto deixou de ficar em `styles/styles.css`: o código-fonte agora está em `assets/scss/` e o `assets/css/style.css` é gerado pelo comando `npm run sass`. O `style.css` é versionado porque o `node_modules` não vai para o repositório e as páginas dependem dele.

"""
    t = t.replace("styles/styles.css", "assets/css/style.css")
    t, n = re.subn(r"## 11\..*?(?=## 12\.)", lambda m: secao11, t, count=1, flags=re.S)
    assert n == 1, "secao 11 do architecture.md nao encontrada"
    linhas = []
    for l in t.split("\n"):
        if re.match(r"\|\s*Sass\s*\|", l):
            l = l.replace("Planejado", "Em uso (Sass)")
        linhas.append(l)
    t = "\n".join(linhas)
    sub = """### 13.6. Estilos com Sass

Os estilos do projeto são escritos em Sass (sintaxe SCSS) em `assets/scss/` e compilados para `assets/css/style.css`. As páginas carregam apenas esse arquivo, depois do CSS do Bootstrap.

| Arquivo | Conteúdo |
| --- | --- |
| `_variables.scss` | Variáveis de cor, tipografia, espaçamento e foco |
| `_mixins.scss` | Mixins reutilizáveis (`foco-anel`, `foco-campo`) |
| `_base.scss` | Tema sobre as variáveis `--bs-*` do Bootstrap, rolagem por âncoras e tipografia |
| `_components.scss` | Botões, categorias (nav pills) e campos de formulário |
| `_layout.scss` | Blocos de layout, como o banner de chamada |
| `main.scss` | Arquivo principal, que importa os módulos com `@use` |

Comandos: `npm run sass` compila uma vez; `npm run sass:watch` recompila a cada alteração. Nunca edite o `assets/css/style.css` à mão, pois ele é sobrescrito na próxima compilação.
"""
    if "## 13." in t:
        t = t.rstrip() + "\n\n" + sub
    else:
        t = t.rstrip() + "\n\n## 13. Estilos com Sass\n\n" + sub.split("\n", 2)[2]
    arq.write_text(t, encoding="utf-8")
    print("atualizado: docs/architecture.md")
print("\nconcluido. Depois de conferir o visual, remova a pasta antiga: git rm -r styles")
