# Atividade Prática — Calculadora de Notas

> **Objetivo:** praticar escrita de testes para encontrar bugs e implementar novos requisitos seguindo o ciclo TDD.

---

## Configuração do ambiente

```bash
# 1. Entre na pasta do projeto

# 2. Crie o ambiente virtual
python -m venv .venv

# 3. Ative o ambiente
source .venv/bin/activate      # Linux/Mac
.venv\Scripts\activate         # Windows

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Confirme que o pytest está funcionando
pytest
```

> Os testes passam porque estão vazios (`pass`). Sua missão é preenchê-los.

---

## Estrutura do projeto

```
projeto/
├── src/
│   └── aluno/
│       ├── __init__.py
│       └── aluno.py       ← código com bugs (não altere ainda)
├── tests/
│   ├── conftest.py              ← fixtures prontas para usar
│   └── unit/
│       └── test_aluno.py  ← seus testes ficam aqui
├── pytest.ini
└── requirements.txt
```

---

## O código

A classe `Aluno` já está implementada em `src/aluno/aluno.py`:

```python
class Aluno:
    def __init__(self, nome: str, notas: list, faltas: int = 0):
        self.nome = nome
        self.notas = notas
        self.faltas = faltas

    def calcular_media(self) -> float:
        ...

    def situacao(self) -> str:
        ...

    def maior_nota(self) -> float:
        ...

    def menor_nota(self) -> float:
        ...

    def calcular_media_arredondada(self) -> float:
        ...
```

O código **roda sem erros** — mas possui **4 bugs escondidos**.

---

## Fixtures disponíveis

No `conftest.py` já existem dois objetos prontos para usar nos testes:

```python
# aluno com notas boas
def test_exemplo(aluno_aprovado):
    print(aluno_aprovado.nome)   # "Maria"
    print(aluno_aprovado.notas)  # [8, 9, 7, 8]

# aluno com notas baixas
def test_exemplo(aluno_reprovado):
    print(aluno_reprovado.nome)   # "João"
    print(aluno_reprovado.notas)  # [4, 3, 5, 4]
```

---

## Como rodar os testes

```bash
# rodar todos
pytest

# rodar e ver detalhes
pytest -v

# ver cobertura ao final
pytest --cov=src --cov-report=term-missing
```

---

---

# PARTE 1 — Encontre os bugs

> **Regra:** abra apenas o arquivo `tests/unit/test_aluno.py`.
> Não altere o `calculadora.py` ainda.

---

## Como funciona

Você vai escrever um teste, rodar o pytest, e observar se ele **falha**.

Se o teste falhar → você encontrou o bug.
Se o teste passar → o teste não está cobrindo o caso certo, tente outro valor.


## Após encontrar todos os bugs

Corrija o `aluno.py` e rode os testes novamente. Todos devem passar.

```bash
pytest tests/unit/test_aluno.py -v
```

---

# PARTE 2 — Implemente com TDD

> **Regra do TDD:** escreva o teste **antes** do código de produção.
> O ciclo é sempre: 🔴 RED → 🟢 GREEN → 🟡 REFACTOR

---

## O ciclo na prática

```
🔴 RED     → escreva o teste (ele deve FALHAR)
🟢 GREEN   → escreva o mínimo de código para passar
🟡 REFACTOR → melhore o código sem quebrar os testes
```

> **Nunca pule o RED.** Se o teste passou sem você escrever o código — o teste está errado.

## Requisito 1 — Contar aprovados

> **Pré-requisito:** confirme que os testes da Parte 1 estão passando antes de começar. Este requisito depende da correção do Bug 2.

**O que deve fazer:**
Uma função que recebe uma lista de alunos e retorna quantos deles estão aprovados.

**Casos que você deve testar:**
- Uma lista em que todos os alunos estão aprovados
- Uma lista em que todos os alunos estão reprovados
- Uma lista mista, com alguns aprovados e outros reprovados
- Uma lista vazia

---

## Requisito 2 — Situação final considerando faltas

**O que deve fazer:**
Um novo comportamento do aluno que considera também as faltas na situação final, seguindo esta ordem de verificação:

1. Se o percentual de faltas (faltas dividido pelo total de aulas) for **maior que 25%**, o aluno é reprovado por falta — independente da média.
2. Caso contrário, se a média for maior ou igual a 6.0, o aluno é aprovado.
3. Caso contrário, o aluno é reprovado por nota.

> Atenção: a regra é "maior que 25%", não "maior ou igual". Um aluno com exatamente 25% de faltas **não** é reprovado por falta — a verificação segue para a média.

**Casos que você deve testar:**
- Um aluno com faltas acima de 25% (deve ser reprovado por falta, mesmo com média alta)
- Um aluno com poucas faltas e média alta (deve ser aprovado)
- Um aluno com poucas faltas e média baixa (deve ser reprovado por nota)
- Um aluno com faltas exatamente em 25% (deve seguir para a verificação da média, não ser reprovado por falta automaticamente)
- Um aluno com faltas pouco acima de 25% (deve ser reprovado por falta)

---

## Requisito 3 — Envio de boletim por e-mail

**O que deve fazer:**
Um novo comportamento do aluno que aciona um serviço externo de envio de e-mail, mas apenas quando o aluno está reprovado.

**Regras:**
- Se o aluno estiver reprovado, o serviço de e-mail deve ser chamado, passando o nome do aluno e sua média.
- Se o aluno estiver aprovado, o serviço de e-mail não deve ser chamado de forma alguma.

**Por que isso exige um cuidado especial:**
O serviço de e-mail é externo — na vida real ele dispararia uma mensagem de verdade. Nos testes, isso não pode acontecer. Por isso, você vai simular esse serviço com um objeto falso (Mock), que permite verificar se ele foi chamado ou não, sem nunca enviar nada de verdade.

**Casos que você deve testar:**
- Um aluno reprovado deve acionar o serviço de e-mail
- Um aluno aprovado não deve acionar o serviço de e-mail

---

## Ao finalizar

Confirme que todos os testes da Parte 1 e da Parte 2 estão passando antes de entregar a atividade.
