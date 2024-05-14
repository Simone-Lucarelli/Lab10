from database.DB_connect import DBConnect
from model.border import Border
from model.country import Country

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllBorders():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from contiguity"""
        cursor.execute(query)
        borders = []
        for row in cursor:
            borders.append(Border(row["state1no"], row["state1ab"], row["stato2no"], row["state2ab"], row["year"]))
        cursor.close()
        cnx.close()
        return borders

    @staticmethod
    def getBorders(year):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from contiguity where year <= %s and conttype=1 order by year"""
        cursor.execute(query, (year,))
        borders = []
        for row in cursor:
            borders.append(Border(row["state1no"], row["state1ab"], row["state2no"], row["state2ab"], row["year"]))
        cursor.close()
        cnx.close()
        return borders

    @staticmethod
    def getCountries():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from country"""
        cursor.execute(query)
        countries = []
        for row in cursor:
            countries.append(Country(row["CCode"], row["StateAbb"], row["StateNme"]))
        cursor.close()
        cnx.close()
        return countries