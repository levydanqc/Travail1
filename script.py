""" Script d'ajout de données depuis un fichier .csv à une base de données MySQL. """
import mysql.connector
from database import read_data


def obtenir_connexion():
    """ Connexion à la base de données MySQL.
        Retourne la connexion active.
    """
    conn = mysql.connector.connect(
        user="root",
        password="mysqlRoot",
        host="127.0.0.1",
        port=3306,
        database="travail1"
    )
    return conn


def ajouter_produit(produit: tuple, curseur):
    """ Ajout de données à la BD

        Args
        ----
        produit (tuple): Données d'un produit
    """
    query = '''insert into produits values
        (%s, "%s", "%s", "%s", "%s", "%s", %s, %s, "%s", "%s", "%s", "%s", "%s", "%s", %s, %s);'''
    cmd = query % produit
    curseur.execute(cmd)


def main():
    """ Fonction principale d'ajout de données dans la bd. """
    connexion = obtenir_connexion()
    curseur = connexion.cursor()

    for produit in read_data("produits.csv"):
        ajouter_produit(produit, curseur)

    connexion.commit()

    curseur.close()
    connexion.close()


if __name__ == "__main__":
    main()
