class Departamento:
    def __init__(self, name, profs=[]):
        self.name = name
        self.profs = profs

    def listar_profs(self):
        print(self.name, ': ', ', '.join(p.name for p in self.profs), sep='')
