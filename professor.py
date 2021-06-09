class Professor:
    def __init__(self, name):
        self.name = name

    def registrar_notas(self, disc):
        print(self.name, 'registrando notas de', disc.name)
