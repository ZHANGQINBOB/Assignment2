import pymysql


class datas:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    passwd='123456',
                                    charset='utf8'
                                    )

        # Use the cursor() method to create a cursor object cursor
        # Select database
        cursor = self.conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS test")
        cursor.execute("USE test")

        # Create Table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS history (
            history_column VARCHAR(20)
        )
        """
        cursor.execute(create_table_query)

    def insert_data(self, data):
        insert_data_query = "INSERT INTO history (history_column) VALUES (%s)"
        cursor = self.conn.cursor()
        print(data)
        cursor.execute(insert_data_query, (data,))
        self.conn.commit()

    def read_data(self):
        select_data_query = "SELECT history_column FROM history"
        cursor = self.conn.cursor()
        cursor.execute(select_data_query)
        data = cursor.fetchall()

        # Extract expression and result from each row
        result = [row[0] for row in data]

        return result