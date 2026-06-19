import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno
import aluno.aluno as aluno_module


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

# Testes para contar_aprovados
def test_contar_aprovados_com_lista_vazia():
    assert aluno_module.contar_aprovados([]) == 0

def test_contar_aprovados_deve_retornar_total_quando_todos_estiverem_aprovados():
    alunos = [
        Aluno(nome="Ana", notas=[7, 7, 7, 7]),
        Aluno(nome="Bia", notas=[8, 8, 8, 8]),
    ]

    assert aluno_module.contar_aprovados(alunos) == 2

def test_contar_aprovados_deve_retornar_zero_quando_todos_estiverem_reprovados():
    alunos = [
        Aluno(nome="Carlos", notas=[4, 4, 4, 4]),
        Aluno(nome="Diana", notas=[5, 5, 5, 5]),
    ]

    assert aluno_module.contar_aprovados(alunos) == 0

def test_contar_aprovados_deve_contar_apenas_aprovados_em_lista_mista():
    alunos = [
        Aluno(nome="Ana", notas=[7, 7, 7, 7]),
        Aluno(nome="Carlos", notas=[5, 5, 5, 5]),
        Aluno(nome="Bia", notas=[6, 6, 6, 6]),
    ]

    assert aluno_module.contar_aprovados(alunos) == 2


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método

def test_situacao_final_deve_reprovar_por_falta_quando_percentual_for_maior_que_25():
    aluno = Aluno(nome="Ana", notas=[9, 9, 9, 9], faltas=3)

    assert aluno.situacao_final(total_aulas=10) == "Reprovado por falta"


def test_situacao_final_deve_aprovar_quando_media_for_suficiente_e_faltas_nao_excederem_25():
    aluno = Aluno(nome="Bia", notas=[7, 7, 7, 7], faltas=2)

    assert aluno.situacao_final(total_aulas=10) == "Aprovado"


def test_situacao_final_deve_reprovar_por_nota_quando_media_for_insuficiente():
    aluno = Aluno(nome="Carlos", notas=[5, 5, 5, 5], faltas=2)

    assert aluno.situacao_final(total_aulas=10) == "Reprovado por nota"


def test_situacao_final_deve_avaliar_media_quando_faltas_for_exatamente_25_porcento():
    aluno = Aluno(nome="Diana", notas=[6, 6, 6, 6], faltas=2)

    assert aluno.situacao_final(total_aulas=8) == "Aprovado"


def test_situacao_final_deve_reprovar_por_falta_quando_percentual_for_pouco_maior_que_25():
    aluno = Aluno(nome="Eva", notas=[8, 8, 8, 8], faltas=3)

    assert aluno.situacao_final(total_aulas=11) == "Reprovado por falta"


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
