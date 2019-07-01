class City(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbors(self, citys):
        self.neighbors.extend(citys)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def search(initial_city, goal):
    frontier = [initial_city]
    explored = set()

    while True:
        print(frontier)

        if len(frontier) == 0:
            return False

        current_city = choose_city(frontier)
        explored.add(current_city)

        if current_city == goal:
            return current_city

        for city in current_city.neighbors:
            if city not in explored and city not in frontier:
                frontier.append(city)


def choose_city(frontier):
    return frontier.pop()


joao_pessoa = City("João Pessoa")
campina_grande = City("Campina Grande")
itabaiana = City("Itabaiana")
santa_rita = City("Santa Rita")
mamanguape = City("Mamanguape")
guarabira = City("Guarabira")
areia = City("Areia")
picui = City("Picui")
soledade = City("Soledade")
coxixola = City("Coxixola")
patos = City("Patos")
monteiro = City("Monteiro")
catole = City("Catolé do Rocha")
pombal = City("Pombal")
itaporanga = City("Itaporanga")
sousa = City("Sousa")
cajazeiras = City("Cajazeiras")

joao_pessoa.add_neighbors([campina_grande, itabaiana, santa_rita])
campina_grande.add_neighbors([joao_pessoa, itabaiana, areia, coxixola, soledade])
itabaiana.add_neighbors([joao_pessoa, campina_grande])
santa_rita.add_neighbors([joao_pessoa, mamanguape])
mamanguape.add_neighbors([santa_rita, guarabira])
guarabira.add_neighbors([mamanguape, areia])
areia.add_neighbors([guarabira, campina_grande])
picui.add_neighbors([soledade])
soledade.add_neighbors([campina_grande, patos, picui])
coxixola.add_neighbors([campina_grande, monteiro])
patos.add_neighbors([soledade, pombal, itaporanga])
monteiro.add_neighbors([coxixola, itaporanga])
catole.add_neighbors([pombal])
pombal.add_neighbors([catole, patos, sousa])
itaporanga.add_neighbors([patos, monteiro])
sousa.add_neighbors([pombal])
# cajazeiras.add_neighbors([sousa, itaporanga])

result = search(joao_pessoa, cajazeiras)
print(result)
