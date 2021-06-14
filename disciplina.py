class Disciplina:
    def __init__(self, name):
        self.name = name

    def ser_ministrada(self, *profs):
        for prof in profs[:5]:
            print(self.name, 'sendo ministrada por', prof.name)
