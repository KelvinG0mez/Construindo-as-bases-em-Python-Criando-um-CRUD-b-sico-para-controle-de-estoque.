# 📦 Sistema de Estoque

Sistema de gerenciamento de estoque via terminal, desenvolvido em Python. Permite adicionar, remover e visualizar produtos com controle de valor unitário e quantidade.

---

## 🚀 Funcionalidades

- **Adicionar item** — Cadastra produto com nome, valor unitário e quantidade
- **Remover item** — Remove um produto do estoque pelo nome
- **Visualizar estoque** — Lista todos os produtos com valor e quantidade formatados
- **Interface limpa** — Limpa o terminal entre cada operação para melhor usabilidade
- **Validação de entrada** — Trata erros de tipo com mensagens amigáveis

---

## 📈 Evolução do Projeto

### v1 — Versão Inicial
- Estoque em lista simples (`[]`)
- Menu com múltiplos `if` e loop `while True`
- Operações básicas de adicionar, remover e visualizar

### v2 — Versão Melhorada
- Estoque em dicionário (`{}`) com suporte a **valor** e **quantidade** por produto
- Funções separadas para cada operação (`adicionar_item`, `remover_item`, `visualizar_estoque`)
- Limpeza de tela automática com `limpar_tela()` (compatível com Windows e Linux/Mac)
- Uso de `match/case` (Python 3.10+) no lugar de múltiplos `if`
- Tratamento de exceção `ValueError` ao inserir valores inválidos
- Feedback visual com `time.sleep()` entre as ações
- Verificação se o item existe antes de tentar remover

---

## 🗂️ Estrutura do Projeto

```
Estoque/
└── estoque.py    # Script principal
```

---

## ⚙️ Configuração

### Pré-requisitos

- Python 3.10+ *(necessário para `match/case` da v2)*

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

> Nenhuma dependência externa necessária — apenas bibliotecas padrão do Python (`os`, `time`).

---

## ▶️ Como Usar

```bash
python estoque.py
```

Ao iniciar, o menu principal será exibido:

```
==== E S T O Q U E ====

Escolha uma opção:
[1] ADICIONAR
[2] REMOVER
[3] VIZUALIZAR
[4] SAIR

Digite uma das opções:
```

### Fluxo de Uso

**Adicionar item:**
```
ADICIONAR no ESTOQUE: Arroz
Valor UNIDADE {Arroz}: R$ 8
QUANTIDADE: 50
ITEM ADCIONADO.
```

**Visualizar estoque:**
```
Produto: Arroz | Valor: R$8.00 | Estoque: 50uni
```

**Remover item:**
```
REMOVER do ESTOQUE: Arroz
ITEM REMOVIDO...
```

---

## 🛠️ Tecnologias

- [Python](https://www.python.org/) — Linguagem principal
- `os` — Limpeza de terminal multiplataforma
- `time` — Pausas para melhor experiência do usuário

