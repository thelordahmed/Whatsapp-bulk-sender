from openpyxl import load_workbook
import sqlite3
import csv
import features_controller


class Model:
    def __init__(self):
        self.data_path = "Data\\data.db"
        self.conn = sqlite3.connect(self.data_path)
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

                # [name, phone]
                record = [name, str(row[features_controller.phone_row - 1])]
                # country code check
                if features_controller.country_code is not None:
                    if row[features_controller.country_code - 1] is None:
                        c_code = ""
                    else:
                        c_code = str(row[features_controller.country_code - 1])
                    # [name, phone, country code]
                    record.append(c_code)
                # extra variable check
                if features_controller.extra_var is not None:
                    if row[features_controller.extra_var - 1] is None:
                        extra_variable = ""
                    else:
                        extra_variable = str(row[features_controller.extra_var - 1])
                    # [name, phone, country code(if found), extra variable]
                    record.append(extra_variable)
                datalist.append(tuple(record))
        elif ".csv" in path:
            with open(path, encoding="utf-8") as csvf:
                reader = csv.reader(csvf)
                datalist = []
                for row in reader:
                    # [name, phone]
                    record = [row[features_controller.name_row - 1], str(row[features_controller.phone_row - 1])]
                    if features_controller.country_code is not None:
                        # [name, phone, country code]
                        record.append(str(row[features_controller.country_code - 1]))
                    if features_controller.extra_var is not None:
                        # (name, phone, country code(if found), extra variable)
                        record.append(str(row[features_controller.extra_var - 1]))
                    datalist.append(tuple(record))
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
