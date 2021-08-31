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


def ajouter_produit(pharmacieIdBJC, upc, sap, idItem, description, fournisseur, coutant, prix, categorie, sousDepartement, departement, marque, din, crx, estTaxableFed, estTaxableProv):
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

def validate(produit):
    pass


def main():
    for produit in database.readData("produits.csv"):
        if validate(produit):
            ajouter_produit(produit)


if __name__ == "__main__":
    main()
