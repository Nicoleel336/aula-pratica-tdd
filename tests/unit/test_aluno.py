import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================

# Teste retornar menor nota
def test_menor_nota(aluno_aprovado):
    assert aluno_aprovado.menor_nota() == 7

# Teste calcular média
def test_calcular_media_com_quantidade_variavel_de_notas():
    aluno = Aluno(nome="Nicole", notas=[10,9,8], faltas=1)
    assert aluno.calcular_media() == 9

# Teste calcular média arredondada
def test_calcular_media_arredondada_valor_decimal():
    aluno = Aluno(nome="Carlos", notas=[7.5, 8.5, 6.3, 5.4], faltas=2)
    assert aluno.calcular_media_arredondada() == 7

# Teste aprovação com média exatamente 6.0
def test_aprovacao_com_media_seis():
    aluno = Aluno(nome="Ana", notas=[6, 6, 6, 6], faltas=0)
    assert aluno.situacao() == "Aprovado"

# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
