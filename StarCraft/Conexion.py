import mysql.connector

class DatabaseConnection:
    @staticmethod
    def conectar():
        try:
            conexion = mysql.connector.connect(
                host="127.0.0.1",
                user="root", 
                database="starcraft"
            )
            return conexion
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")
            raise
