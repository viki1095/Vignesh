import sqlite3


class DataBaseFile:

    def __init__(self, file_name):
        self.file_name = file_name

    def get_connection(self):
        con = sqlite3.connect(self.file_name)
        print('Created Table')
        return con

    def create_table(self, con, table_name):
        con.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}(Name, Class, Marks, Grade)''')
        print("Table Created")

    def insert_records(self, con, table_name, obj):
        data = f''' INSERT INTO {table_name}(Name, Class, Marks, Grade) VALUES(?, ?, ?, ?)'''
        con.execute(data, (obj.name, obj.cls, obj.mark, obj.grade))
        con.commit()
        print("inserted the records")

    def close_connection(self, con):
        con.close()
        print("closed the connection")