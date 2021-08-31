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


def main():
    database.readData("produits.csv")


if __name__ == "__main__":
    main()
