""" Module de lecture de données depuis un fichier csv. """
import os.path as path


def validate(data: tuple):
    """ Validation des données à l'aide de règles prédéfinies.
        Retourne Vrai si les données sont valide en fonction de:
        - DIN est plus grand que 3$
        - Il y a une taxe fédérale et provinciale
        - UPC contient moins de 12 caratères (14 en comptant le ".0" du float)
        - Prix de vente est plus grand que le prix coûtant

        Args
        ----
        data (tuple): Données d'un produit
    """
    return (int(data[-1]) == int(data[-2]) == 1) and (int(data[-4]) > 3) \
        and (len(str(float(data[1]))) <= 14) and (float(data[7]) > float(data[6]))


def read_data(file_name: str):
    """ Vérifie la validité du fichier et retourne une liste de tuple des données
        sur les produits après vérification de leur validité.

        Args
        ----
        file_name (str): Nom du fichier contenant les données
    """
    if path.isfile(file_name) and path.splitext(file_name)[1] == '.csv':
        with open("produits.csv") as file:
            return [x for i in file if
                    validate(x := tuple(i.replace(',', '.').replace('\n', '').split(';')))]
    else:
        raise ValueError("Le nom du fichier n'est pas valide.")


def print_data():
    """ Fonction de test à des fin de débugging. """
    with open("produits.csv") as file:
        print([tuple(i.replace('\n', '').split(';')) for i in file][5][-1])


if __name__ == "__main__":
    print_data()
