""" Module de lecture de données depuis un fichier csv. """
import os.path as path


def validate(data: tuple):
    """ Validation des données à l'aide de règles prédéfinies.
        Retourne Vrai si les données sont invalide en fonction de:
        - DIN est plus petit que 3$
        - Aucune taxe fédérale ou provinciale
        - UPC contient plus de 12 caratères (14 en comptant le ".0" du float)
        - Prix de vente est plus petit que le prix coûtant

        Args
        ----
        data (tuple): Données d'un produit
    """
    return (int(data[-4]) < 3) or (int(data[-1]) == int(data[-2]) == 0) \
        or (len(str(float(data[1]))) < 14) or (float(data[7]) < float(data[6]))


def read_data(file_name: str):
    """ Vérifie la validité du fichier et retourne une liste de tuple des données
        sur les produits après vérification de leur validité.

        Args
        ----
        file_name (str): Nom du fichier contenant les données
    """
    if path.isfile(file_name) and path.splitext(file_name)[1] == '.csv':
        with open("produits.csv") as file:
            return [x for i in file if not
                    validate(x := tuple(i.replace(',', '.').replace('\n', '').split(';')))]
    else:
        raise ValueError("Le nom du fichier n'est pas valide.")


def print_data():
    """ Fonction de test à des fin de débugging. """
    with open("produits.csv") as file:
        print([tuple(i.replace('\n', '').split(';')) for i in file][5][-1])


if __name__ == "__main__":
    print_data()
