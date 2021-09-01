""" Script d'ajout de données depuis un fichier .csv à une base de données MySQL. """
import mysql.connector
import database


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


def ajouter_produit(produit: tuple):
    """ Ajout de données à la BD

        Args
        ----
        produit (tuple): Données d'un produit
    """
    connexion = obtenir_connexion()
    curseur = connexion.cursor()
    query = 'insert into produits values' + \
        '(%s, "%s", "%s", "%s", "%s", "%s", %s, %s, "%s", "%s", "%s", "%s", "%s", "%s", %s, %s);'
    cmd = query % produit
    curseur.execute(cmd)

    connexion.commit()

    curseur.close()
    connexion.close()


def main():
    """ Fonction principale d'ajout de données dans la bd. """
    for produit in database.read_data("produits.csv"):
        ajouter_produit(produit)


if __name__ == "__main__":
    main()
