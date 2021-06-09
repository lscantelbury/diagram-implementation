from disciplina import Disciplina
from professor import Professor
from universidade import Universidade

# --- DISCIPLINAS --- #

intro_redes = Disciplina('Introdução a Redes de Computadores')
sistemas_operacionais = Disciplina('Sistemas Operacionais')
modelagem_banco = Disciplina('Modelagem de Banco de Dados')

fisico_quimica = Disciplina('Fisico Quimica')
estudo_gases = Disciplina('Estudo dos Gases')

efeitos_guerra = Disciplina('Efeitos da Segunda Guerra')
governo_color = Disciplina('Governos Brasileiros: Governo Color')
regime_militar = Disciplina('Regime Militar')
indep_americana = Disciplina('Independencia Americana')

calculo_2 = Disciplina('Calculo II')

# --- PROFESSORES --- #

jeferson = Professor('Jeferson Solza')
pedro = Professor('Pedro Alberto')
jucimar = Professor('Jucimar Junior')
glauco = Professor('Glauco Denis')
rodrigo = Professor('Ridrigo Neves')
filipe = Professor('Felipe da Cunha')
olavo = Professor('Olavo de Carvalho')
julia = Professor('Julia Gonsalves')
paula = Professor('Paula Ferreira')
diana = Professor('Diana Janny')
maria = Professor('Maria das Grassas')
antonia = Professor('Antonia Silva')
marta = Professor('Marta Guerra')

# --- UNIVERSIDADE --- #

univ = Universidade("Universidade Municipal de Manaus")
univ.sistemas.profs = jeferson, jucimar, diana, marta
univ.quimica.profs = maria, pedro
univ.historia.profs = julia, olavo, filipe
univ.exatas.profs = rodrigo, paula, antonia, glauco

# --- USO DAS RELACOES --- #

## ASSOCIACAO
intro_redes.ser_ministrada(jeferson)
governo_color.ser_ministrada(julia)
governo_color.ser_ministrada(filipe)
maria.registrar_notas(estudo_gases)
maria.registrar_notas(fisico_quimica)
antonia.registrar_notas(calculo_2)
rodrigo.registrar_notas(calculo_2)

## AGREGACAO
univ.exatas.listar_profs()

## COMPOSICAO
univ.listar_profs_de_sistemas_com_j()
