class Professor:
    def __init__(self, name):
        self.name = name

    def registrar_notas(self, *discs):
        for disc in discs[:5]:
            print(self.name, 'registrando notas de', disc.name)
