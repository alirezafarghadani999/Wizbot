import sqlite3
import os

class SqliteHandler:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        """Establish a connection to the SQLite database."""
        if not os.path.exists(self.db_name):
            self.create_database()
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_database(self):
        """Create a new SQLite database."""
        with sqlite3.connect(self.db_name) as conn:
            pass  # The database file is created automatically if it does not exist

    def create_table(self, table_name, columns):
        """
        Create a table in the SQLite database.
        
        :param table_name: Name of the table to create
        :param columns: Dictionary of column names and their types, e.g., {"id": "INTEGER PRIMARY KEY", "name": "TEXT"}
        """
        columns_definition = ", ".join([f"{col} {col_type}" for col, col_type in columns.items()])
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition})"
        self.cursor.execute(create_table_sql)
        self.connection.commit()

    def insert_record(self, table_name, record):
        """
        Insert a record into a table.
        
        :param table_name: Name of the table to insert into
        :param record: Dictionary of column names and values, e.g., {"name": "John", "age": 30}
        """
        columns = ", ".join(record.keys())
        placeholders = ", ".join(["?"] * len(record))
        insert_sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(insert_sql, tuple(record.values()))
        self.connection.commit()

    def remove_record(self, table_name, condition):
        """
        Remove a record from a table.
        
        :param table_name: Name of the table to remove from
        :param condition: Condition to match for deletion, e.g., "id = 1"
        """
        delete_sql = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(delete_sql)
        self.connection.commit()

    def search_record(self, table_name, condition):
        """
        Search for records in a table.
        
        :param table_name: Name of the table to search in
        :param condition: Condition to match for searching, e.g., "age > 20"
        :return: List of matching records
        """
        search_sql = f"SELECT * FROM {table_name} WHERE {condition}"
        self.cursor.execute(search_sql)
        return self.cursor.fetchall()

    def close(self):
        """Close the connection to the SQLite database."""
        if self.connection:
            self.connection.close()
