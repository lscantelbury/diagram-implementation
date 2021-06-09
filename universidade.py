from departamento import Departamento


class Universidade:
    def __init__(self, name):
        self.name = name

        self.sistemas = Departamento('Sistemas')
        self.quimica = Departamento('Quimica')
        self.historia = Departamento('Historia')
        self.exatas = Departamento('Exatas')

    def listar_profs_de_sistemas_com_j(self):
        print('profs de Sistemas com J: ')
        
        found = False

        for prof in self.sistemas.profs:
            if 'j' in prof.name.lower():
                print(prof.name, end=' ')
                found = True

        if not found:
            print('N/A')
