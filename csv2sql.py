#!/usr/bin/env python3

import mysql.connector as mcnx
from getpass import getpass
import csvutils as csv

csvfile = "/home/andy/Downloads/und2data.csv"

def checkSQLData(data):
    SQLkeys = (";", "DROP", "INSERT", "GRANT", "CREATE", "drop", "insert", "grant", "create")
    for entry in data:
        for elem in entry:
            if (any(SQLkeys) for c in elem):
                print("[warn] SQL injection possible for element: ", elem)
def main():
    # cnx = mcnx.connect(user='andy', password=getpass(), host='127.0.0.1', database='iste151')
    # c = cnx.cursor()
    data = csv.createEntryList(csvfile)
    csv.tfToInt('True', 'False', data)
    csv.tfToInt('yes', 'no', data)
    for point in data:
        if len(point) < 195:
            print(point)
        print((point))
    # c.close()
    # cnx.close()


if __name__ == '__main__':
    main()
