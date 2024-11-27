# Importación de las clases necesarias para el manejo de la base de datos y la herencia
from BaseModel import BaseModel  
from Conexion import DatabaseConnection  
import mysql.connector  

class Partida(BaseModel):
    def __init__(self):
        # Iniciar la conexión a la base de datos al crear una instancia de Partida
        self.conexion = DatabaseConnection.conectar()

    def crear(self):
        # Crear una partida en la base de datos
        cursor = self.conexion.cursor()

        print("\n=== CREAR PARTIDA ===")
        # Solicitar los datos de la partida
        tipo = input("Ingrese el tipo de partida (Clasificatoria, Amistosa, Cooperativa): ")
        jugadores = int(input("Ingrese el número de jugadores: "))
        mapa = input("Ingrese el mapa: ")

        try:
            # Insertar los datos de la partida en la base de datos
            sql = "INSERT INTO partidas (tipo_partida, numero_jugadores, mapa) VALUES (%s, %s, %s)"
            valores = (tipo, jugadores, mapa)
            cursor.execute(sql, valores)
            self.conexion.commit()  # Confirmar los cambios

            # Mostrar el ID de la nueva partida
            print(f"Partida creada exitosamente con ID {cursor.lastrowid}")
        except mysql.connector.Error as err:
            # Manejar errores de MySQL
            print(f"Error: {err}")
        finally:
            # Cerrar el cursor y la conexión a la base de datos
            cursor.close()


    def listar(self):
        # Función para listar todas las partidas registradas
        cursor = self.conexion.cursor()
    
        print("\n=== LISTAR PARTIDAS ===")
        try:
            # Ejecutar la consulta para obtener todas las partidas
            sql = "SELECT * FROM partidas ORDER BY fecha_creacion DESC"
            cursor.execute(sql)
            resultados = cursor.fetchall()  # Obtener todos los resultados
    
            # Si hay partidas, mostrarlas
            if resultados:
                for partida in resultados:
                    print(f"ID: {partida[0]}, Tipo: {partida[1]}, Jugadores: {partida[2]}, Mapa: {partida[3]}, Fecha: {partida[4]}")
            else:
                print("No se encontraron partidas registradas.")
        except mysql.connector.Error as err:
            # Manejar errores de MySQL
            print(f"Error: {err}")
        finally:
            # Cerrar el cursor y la conexión
            cursor.close()


    def actualizar(self):
        # Función para actualizar los detalles de una partida
        cursor = self.conexion.cursor()


        print("\n=== ACTUALIZAR DETALLES DE UNA PARTIDA ===")
        # Solicitar el ID de la partida a actualizar
        id_partida = input("Ingrese el ID de la partida que desea actualizar: ")

        cursor.execute("SELECT * FROM partidas WHERE id_partida = %s", (id_partida,))
        partida = cursor.fetchone()  # Buscar la partida por su ID

        # Verificar si la partida existe
        if not partida:
            print("No se encontró una partida con ese ID.")
            cursor.close()
            return

        # Mostrar los detalles de la partida encontrada
        print(f"Partida encontrada: ID: {partida[0]}, Tipo: {partida[1]}, Jugadores: {partida[2]}, Mapa: {partida[3]}")

        # Solicitar los nuevos datos (o dejar los actuales si no se desean cambios)
        nuevo_tipo = input("Ingrese el nuevo tipo de partida (Clasificatoria, Amistosa, Cooperativa) (o presione Enter para no cambiar): ")
        nuevo_num_jugadores = input("Ingrese el nuevo número de jugadores (o presione Enter para no cambiar): ")

        # Preparar la consulta de actualización
        sql = "UPDATE partidas SET "
        valores = []
        if nuevo_tipo:
            sql += "tipo_partida = %s, "
            valores.append(nuevo_tipo)
        if nuevo_num_jugadores:
            sql += "numero_jugadores = %s, "
            valores.append(nuevo_num_jugadores)

        # Eliminar la coma final y agregar la condición WHERE para el ID de la partida
        sql = sql.rstrip(", ") + " WHERE id_partida = %s"
        valores.append(id_partida)

        try:
            # Ejecutar la consulta de actualización
            cursor.execute(sql, tuple(valores))
            self.conexion.commit()  # Confirmar los cambios
            print("Partida actualizada exitosamente.")
        except mysql.connector.Error as err:
            # Manejar errores de MySQL
            print(f"Error: {err}")
        finally:
            # Cerrar el cursor y la conexión
            cursor.close()


    def eliminar(self):
        # Función para eliminar una partida
        cursor = self.conexion.cursor()


        print("\n=== ELIMINAR PARTIDA ===")
        # Solicitar el ID de la partida a eliminar
        id_partida = input("Ingrese el ID de la partida que desea eliminar: ")

        cursor.execute("SELECT * FROM partidas WHERE id_partida = %s", (id_partida,))
        partida = cursor.fetchone()  # Buscar la partida por su ID

        # Verificar si la partida existe
        if not partida:
            print("No se encontró una partida con ese ID.")
            cursor.close()
            return

        # Mostrar los detalles de la partida encontrada
        print(f"Partida encontrada: ID: {partida[0]}, Tipo: {partida[1]}, Jugadores: {partida[2]}, Mapa: {partida[3]}")
        confirmacion = input("¿Está seguro que desea eliminar esta partida? (S/N): ").strip().upper()

        # Confirmar la eliminación
        if confirmacion == "S":
            try:
                # Ejecutar la consulta de eliminación
                cursor.execute("DELETE FROM partidas WHERE id_partida = %s", (id_partida,))
                self.conexion.commit()  # Confirmar los cambios
                print("Partida eliminada exitosamente.")
            except mysql.connector.Error as err:
                # Manejar errores de MySQL
                print(f"Error: {err}")
        else:
            print("Eliminación cancelada.")

        # Cerrar el cursor y la conexión
        cursor.close()
