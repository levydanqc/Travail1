""" Module for reading data from a file"""
import os.path as path


def readData(fileName: str):
    """ Read file data and return tuple if file is valid

        Args
        ----
        fileName (str): Name of the file where the data is stored
    """
    if path.isfile(fileName) and path.splitext(fileName) == "csv":
        with open("produits.csv") as file:
            return [tuple(i.replace('\n', '').split(';')) for i in file]


def printData():
    with open("produits.csv") as file:
        print([tuple(i.replace('\n', '').split(';')) for i in file][0])


if __name__ == "__main__":
    printData()
