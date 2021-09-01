""" Module for reading data from a file"""
import os.path as path


def validate(data: tuple):
    """ Validation of data from certain rules.
        Return True if data is not valid from:
        - DIN is less than 3$
        - No federal or provincial taxes
        - UPC is longer than 12 charn (14 when counting ".0" from float)
        - Sell price is lower than cost

        Args
        ----
        data (tuple): Tuple of data product
    """
    a = (int(data[-4]) < 3) or (int(data[-1]) == int(data[-2]) == 0) \
                or (len(str(float(data[1].replace(",", ".")))) < 14) \
                or (float(data[7].replace(",", ".")) < float(data[6].replace(",", ".")))
    if a is False:
        print(a);
    return a;

def readData(fileName: str):
    """ Read file data and return tuple if file is valid

            Args
            ----
            fileName (str): Name of the file where the data is stored
    """
    if path.isfile(fileName) and path.splitext(fileName)[1] == ".csv":
        with open("produits.csv") as file:
            return [x for i in file if not validate(x := tuple(i.replace('\n', '').split(';')))]


def printData():
    """ Print data for test purposes """
    with open("produits.csv") as file:
        print([tuple(i.replace('\n', '').split(';')) for i in file][5][-1])


if __name__ == "__main__":
    printData()
