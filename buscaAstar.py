class City(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbors(self, citys):
        for city in citys:
            self.neighbors.append({"city": city[0], "cost": city[1], "estimate": city[2]})

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

def search(initial_city, goal):
    frontier = [{"city": initial_city, "cost": 0, "estimate": 460, "parent": None}]
    explored = set()
    couter = 0


    while True:
        couter += 1
        print("Passo",couter,end="")
        print(".")

        if len(frontier) == 0:
            return False

        print_borders(frontier)

        chosen = choose_city(frontier)
        explored.add(chosen["city"])

        print("Explorado: ",chosen["city"])
        print()

        if chosen["city"] == goal:
            return chosen

        for neighbor in chosen["city"].neighbors:

            path_cost = neighbor["cost"] + chosen["cost"]
            path_estimate_value = neighbor["estimate"] + path_cost

            if neighbor["city"] in explored:
                continue
            else:
                flag = False
                for node in frontier:
                    if neighbor["city"] == node["city"]:
                        flag = True

                        if node["estimate"] > path_estimate_value:
                            frontier.remove(node)
                            frontier.append({"city": neighbor["city"], "cost": path_cost,"estimate": path_estimate_value, "parent": chosen})
                if flag == False:
                    frontier.append({"city": neighbor["city"], "cost": path_cost, "estimate": path_estimate_value, "parent": chosen})

def choose_city(frontier):
    lower_estimate_node = frontier[0]

    for node in frontier:
        if node["estimate"] < lower_estimate_node["estimate"]:
            lower_estimate_node = node
    frontier.remove(lower_estimate_node)
    return lower_estimate_node

def print_borders(explored_frontier):
    size = 1
    print("Fronteira: ",end="")

    for borders in explored_frontier:
        print(borders["city"], end="")
        print(": ",borders["estimate"],end="")
        if size  == len(explored_frontier):
            continue
        else:
            size += 1
            auxiliary_size = size -2
            if auxiliary_size < len(explored_frontier):
                print(", ",end="")
    print()


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

joao_pessoa.add_neighbors([[campina_grande, 125, 300], [itabaiana, 68, 360], [santa_rita, 26, 451]])
campina_grande.add_neighbors([[joao_pessoa, 125, 460], [itabaiana, 65, 360], [areia, 40, 316], [coxixola, 128, 232], [soledade, 58, 243]])
itabaiana.add_neighbors([[joao_pessoa, 68, 460], [campina_grande, 65, 300]])
santa_rita.add_neighbors([[joao_pessoa, 26, 460], [mamanguape, 38, 380]])
mamanguape.add_neighbors([[santa_rita, 38, 451], [guarabira, 42, 340]])
guarabira.add_neighbors([[mamanguape, 42, 380], [areia, 41, 316]])
areia.add_neighbors([[guarabira, 41, 340], [campina_grande, 40, 300]])
picui.add_neighbors([[soledade, 69, 243]])
soledade.add_neighbors([[campina_grande, 58, 300], [patos, 117, 122], [picui, 69, 260]])
coxixola.add_neighbors([[campina_grande, 128, 300], [monteiro, 83, 195]])
patos.add_neighbors([[soledade, 117, 243], [pombal, 71, 55], [itaporanga, 108, 65]])
monteiro.add_neighbors([[coxixola, 83, 232], [itaporanga, 224, 65]])
catole.add_neighbors([[pombal, 57, 55]])
pombal.add_neighbors([[catole, 57, 110], [patos, 71, 122], [sousa, 56, 20]])
itaporanga.add_neighbors([[patos, 108, 122], [cajazeiras, 121, 0], [monteiro, 224, 195]])
sousa.add_neighbors([[pombal, 56, 55], [cajazeiras, 43, 0]])
cajazeiras.add_neighbors([[sousa, 43, 20], [itaporanga, 121, 65]])

city = search(joao_pessoa, cajazeiras)

path = []
while city != None:
    path.append(city["city"])
    city = city["parent"]

path.reverse
print(path)