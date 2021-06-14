class Departamento:
    def __init__(self, name, profs=[]):
        self.name = name
        self.profs = profs

    @property
    def profs(self):
        return self._profs

    @profs.setter
    def profs(self, vals):
        self._profs = vals[:5]

    def listar_profs(self):
        print(self.name, ': ', ', '.join(p.name for p in self.profs), sep='')
