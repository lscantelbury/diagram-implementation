class Disciplina:
    def __init__(self, name):
        self.name = name

    def ser_ministrada(self, prof):
        print(self.name, 'sendo ministrada por', prof.name)
