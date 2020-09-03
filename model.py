from openpyxl import load_workbook
import sqlite3
import csv
import features_controller




class Model:
    def __init__(self):
        self.conn = sqlite3.connect("Data\\data.db")
        self.cur = self.conn.cursor()


    @staticmethod
    def getDataFromSheet(path):
        """
        :param path: string
        :return: list or rows - list of tuples
        """
        if ".xlsx" in path:
            wb = load_workbook(path)
            sheet = wb.active
            data = sheet.values
            datalist = []
            for row in data:
                # check on empty rows
                if row[features_controller.name_row-1] is None and row[features_controller.phone_row-1] is None:
                    break

                if row[features_controller.name_row-1] is None:
                    name = ""
                else:
                    name = row[features_controller.name_row-1]

                if features_controller.country_code is not None:
                    if row[features_controller.country_code - 1] is None:
                        c_code = ""
                    else:
                        c_code = str(row[features_controller.country_code - 1])

                    # (name, phone, country code)
                    record = (name, str(row[features_controller.phone_row - 1]), c_code)
                    datalist.append(record)
                else:
                    # (name, phone)
                    record = (name, str(row[features_controller.phone_row-1]))
                    datalist.append(record)
        elif ".csv" in path:
            with open(path, encoding="utf-8") as csvf:
                reader = csv.reader(csvf)
                datalist = []

                if features_controller.country_code is not None:
                    for row in reader:
                        # (name, phone, country code)
                        record = (row[features_controller.name_row - 1], str(row[features_controller.phone_row - 1]), str(row[features_controller.country_code - 1]))
                        datalist.append(record)
                else:
                    for row in reader:
                        # (name, phone)
                        record = (row[features_controller.name_row-1], str(row[features_controller.phone_row-1]))
                        datalist.append(record)
        if features_controller.header_row:
            del datalist[0]
        return datalist

    def saveInterfaceValues(self, data):
        """

        :param data: tuple
        :return: None
        """
        with self.conn:
            self.cur.execute("DELETE FROM interface")
            self.cur.execute('''INSERT INTO interface VALUES (?,?,?,?,?,?,?)''', data)

    def getInterfaceValues(self):
        """
        :return: list of tuples
        """
        self.cur.execute('''SELECT * FROM interface''')
        value = self.cur.fetchall()
        # print(value)
        return value

    def addTodata(self, data):
        """
        :param data: a tuple type (name, phone, status)
        :return: None
        """
        with self.conn:
            self.cur.execute('''INSERT INTO sent_contacts VALUES (?,?,?)''', data)

    def findContact(self, phone):
        """
        :param phone: str
        :return: tuple - Nonetype if no data
        """
        self.cur.execute('''SELECT * FROM sent_contacts WHERE phone = (:phone)''', {"phone": phone})
        value = self.cur.fetchone()
        return value

    def getAllRecords(self):
        """:return list of tuples - empty list if no data """
        self.cur.execute('''SELECT name, phone, status FROM sent_contacts''')
        data = self.cur.fetchall()
        return data

    def clearDatabase(self):
        with self.conn:
            self.cur.execute("DELETE FROM sent_contacts")
            self.cur.execute("DELETE FROM interface")

    # def findRecord(self, name, address, phone):
    #     self.cur.execute('''SELECT * FROM data WHERE name = (?) AND address = (?) AND phone = (?)''',
    #                      (name, address, phone))
    #     print(self.cur.fetchone())
