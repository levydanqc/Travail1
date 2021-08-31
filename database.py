""" Module for reading data from a file"""
import os.path as path


def readData(fileName: str):
    """ Read file data and return tuple if file is valid
        
        Args
        ----
        fileName (str): Name of the file where the data is stored
    """
    if path.isfile(fileName) and path.splitext(fileName) == "csv":
        pass


def printData():
    pass


if __name__ == "__main__":
    printData()
