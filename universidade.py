from departamento import Departamento


class Universidade:
    def __init__(self, name):
        self.name = name

        self.sistemas = Departamento('Sistemas')
        self.quimica = Departamento('Quimica')
        self.historia = Departamento('Historia')
        self.exatas = Departamento('Exatas')

    def listar_profs_de_sistemas_com_j(self):
        profs_com_j = []

        for prof in self.sistemas.profs:
            if 'j' in prof.name.lower():
                profs_com_j.append(prof.name)

        print('Profs de Sistemas com J:',
              ', '.join(profs_com_j) if len(profs_com_j) else 'N/A')
