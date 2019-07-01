class City(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbors(self, citys):
        for city in citys:
            self.neighbors.append({"city": city[0], "cost": city[1]})

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def search(initial_city, goal):
    frontier = [{"city": initial_city, "cost": 0, "parent": None}]
    explored = set()

    while True:
        # print(frontier)

        if len(frontier) == 0:
            return False

        chosen = choose_city(frontier)
        explored.add(chosen["city"])

        if chosen["city"] == goal:
            return chosen

        for neighbor in chosen["city"].neighbors:
            path_cost = neighbor["cost"] + chosen["cost"]

            if neighbor["city"] in explored:
                continue
            else:
                flag = False
                for node in frontier:
                    if neighbor["city"] == node["city"]:
                        flag = True

                        if node["cost"] > path_cost:
                            frontier.remove(node)
                            frontier.append({"city": neighbor["city"], "cost": path_cost, "parent": chosen})
                if flag == False:
                    frontier.append({"city": neighbor["city"], "cost": path_cost, "parent": chosen})


def choose_city(frontier):
    lower_cost_node = frontier[0]

    for node in frontier:
        if node["cost"] < lower_cost_node["cost"]:
            lower_cost_node = node
    frontier.remove(lower_cost_node)
    return lower_cost_node


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

joao_pessoa.add_neighbors([[campina_grande, 125], [itabaiana, 68], [santa_rita, 26]])
campina_grande.add_neighbors([[joao_pessoa, 125], [itabaiana, 65], [areia, 40], [coxixola, 128], [soledade, 58]])
itabaiana.add_neighbors([[joao_pessoa, 68], [campina_grande, 65]])
santa_rita.add_neighbors([[joao_pessoa, 26], [mamanguape, 38]])
mamanguape.add_neighbors([[santa_rita, 38], [guarabira, 42]])
guarabira.add_neighbors([[mamanguape, 42], [areia, 41]])
areia.add_neighbors([[guarabira, 41], [campina_grande, 40]])
picui.add_neighbors([[soledade, 69]])
soledade.add_neighbors([[campina_grande, 58], [patos, 117], [picui, 69]])
coxixola.add_neighbors([[campina_grande, 128], [monteiro, 83]])
patos.add_neighbors([[soledade, 117], [pombal, 71], [itaporanga, 108]])
monteiro.add_neighbors([[coxixola, 83], [itaporanga, 224]])
catole.add_neighbors([[pombal, 57]])
pombal.add_neighbors([[catole, 57], [patos, 71], [sousa, 56]])
itaporanga.add_neighbors([[patos, 108], [cajazeiras, 121], [monteiro, 224]])
sousa.add_neighbors([[pombal, 56], [cajazeiras, 43]])
cajazeiras.add_neighbors([[sousa, 43], [itaporanga, 121]])

city = search(joao_pessoa, cajazeiras)

path = []
while city != None:
    path.append(city["city"])
    city = city["parent"]
path.reverse
print(path)
