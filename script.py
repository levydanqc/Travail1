import database
import mysql.connector


def obtenir_connexion():
    conn = mysql.connector.connect(
        user="root",
        password="mysqlRoot",
        host="127.0.0.1",
        port=3306,
        database="travail1"
    )
    return conn


def ajouter_produit(pharmacieIdBJC: str, upc: str, sap: str, idItem: str, description: str, fournisseur: str, coutant: str, prix: str, categorie: str, sousDepartement: str, departement: str, marque: str, din: str, crx: str, estTaxableFed: str, estTaxableProv: str):
    """ Ajout de données à la BD

        Args
        ----
        pharmacieIdBJC (str): # de succursale
        upc (str): Code barre
        sap (str): Numéro du produit
        idItem (str): Code unique pour le produit
        description (str): Description du produit
        fournisseur (str): Numéro du fournisseur
        coutant (str): Coûtant
        prix (str): Prix de vente
        categorie (str): Catégorie du produit
        sousDepartement (str): Sous-département
        departement (str): Département
        marque (str): Marque
        din (str): Drug identification number
        crx (str): Code de prescription
        estTaxableFed (str): Taxe fédérale
        estTaxableProv (str): Taxe provinciale
    """
    connexion = obtenir_connexion()
    curseur = connexion.cursor()
    params = "(pharmacieIdBJC, upc, sap, idItem, description, fournisseur, coutant, prix, categorie, sousDepartement, departement, marque, din, crx, estTaxableFed, estTaxableProv)"
    values = (int(pharmacieIdBJC), upc, sap, idItem, description, fournisseur, float(coutant.replace(',', '.')), float(prix.replace(',', '.')),
              categorie, sousDepartement, departement, marque, din, crx, int(estTaxableFed), int(estTaxableProv))
    query = 'insert into produits %s values (%s, "%s", "%s", "%s", "%s", "%s", %s, %s, "%s", "%s", "%s", "%s", "%s", "%s", %s, %s);'
    cmd = query % (params, *values)
    curseur.execute(query)

    connexion.commit()

    curseur.close()
    connexion.close()



def main():
    for produit in database.readData("produits.csv"):
        ajouter_produit(*produit)


if __name__ == "__main__":
    main()
