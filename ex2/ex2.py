import csv
from rdflib import Namespace, URIRef, Graph, Literal
from rdflib.namespace import RDF, OWL, FOAF

g = Graph()
g.parse("teste/medical_original.ttl")

nmp = Namespace("http://www.example.org/disease-ontology#")

def read_csv_to_dict(file_path):
    result = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            result.append(dict(row))
    return result



def get_instances_diseases():
    counter_s = 0
    for i, row in enumerate(data):

        for i, items in enumerate(row.items()):
            key, value = items[0], items[1]

            if i == 0:
                disease_id = value.replace(" ", "_")
                disease_uri = URIRef(f"{nmp}{disease_id}")
                g.add((disease_uri, RDF.type, nmp.Disease))

            else:

                if value not in symptons.keys():
                    symptom_id = value.replace(" ", "_")
                    symptom_uri = URIRef(f"{nmp}{symptom_id}")
                    symptons[key] = symptom_uri
                else:
                    symptom_uri = symptons[key]

                g.add((symptom_uri, RDF.type, nmp.Symptom)) # Literal(value)))

def create_descriptions():
    for i, row in enumerate(data):
        for i, items in enumerate(row.items()):
            key, value = items[0], items[1]

            if i == 0:
                val = value.replace(" ", "_")
                disease_uri = URIRef(f"{nmp}{val}")
                g.add((disease_uri, RDF.type, nmp.Disease))


def write_in_file():
    with open("teste/medical.ttl", "w") as f_out:
        f_out.write(g.serialize(format="turtle"))

symptons = {}
file_path = 'teste/Disease_Syntoms.csv'
data = read_csv_to_dict(file_path)
get_instances_diseases()

file_path_2 = 'teste/Disease_Description.csv'
#data_descriptions = read_csv_to_dict(file_path_2)
create_descriptions()

write_in_file()
