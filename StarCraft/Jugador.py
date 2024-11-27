from BaseModel import BaseModel
from Conexion import DatabaseConnection
import mysql.connector


class Jugador(BaseModel):
    def __init__(self):
        self.conexion = DatabaseConnection.conectar()

    def crear(self):
        cursor = self.conexion.cursor()

        # Solicitar datos del usuario
        print("\n=== CREAR PERFIL DE JUGADOR ===")
        nombre = input("Ingrese su nombre de usuario: ")
        raza = input("Ingrese su raza preferida (Terran, Zerg, Protoss): ")
        nivel = input("Ingrese su nivel de habilidad (Principiante, Intermedio, Avanzado): ")

        try:
            # Insertar en la base de datos
            sql = "INSERT INTO jugadores (nombre, raza, nivel_habilidad) VALUES (%s, %s, %s)"
            valores = (nombre, raza, nivel)
            cursor.execute(sql, valores)
            self.conexion.commit()

            print(f"Perfil creado exitosamente con ID {cursor.lastrowid}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            self.conexion.close()

    def listar(self):
        cursor = self.conexion.cursor()

        print("\n=== LISTAR PERFILES DE JUGADORES ===")
        filtro = input("¿Desea filtrar por raza o nivel de habilidad? (S/N): ").strip().upper()

        sql = "SELECT * FROM jugadores"
        valor = None

        if filtro == "S":
            criterio = input("Ingrese el criterio de filtro ('raza' o 'nivel'): ").strip().lower()
            valor = input("Ingrese el valor del filtro: ").strip()

            if criterio == "raza":
                sql += " WHERE raza = %s"
            elif criterio == "nivel":
                sql += " WHERE nivel_habilidad = %s"
            else:
                print("Criterio no válido. Mostrando todos los perfiles.")
                valor = None

        try:
            if valor:
                cursor.execute(sql, (valor,))
            else:
                cursor.execute(sql)

            resultados = cursor.fetchall()
            if resultados:
                for jugador in resultados:
                    print(f"ID: {jugador[0]}, Nombre: {jugador[1]}, Raza: {jugador[2]}, Nivel: {jugador[3]}, Fecha: {jugador[4]}")
            else:
                print("No se encontraron jugadores.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()


    def actualizar(self):
        cursor = self.conexion.cursor()

        print("\n=== ACTUALIZAR PERFIL DE JUGADOR ===")
        id_jugador = input("Ingrese el ID del jugador que desea actualizar: ")

        cursor.execute("SELECT * FROM jugadores WHERE id_jugador = %s", (id_jugador,))
        jugador = cursor.fetchone()

        if not jugador:
            print("No se encontró un jugador con ese ID.")
            cursor.close()
            return

        print(f"Jugador encontrado: ID: {jugador[0]}, Nombre: {jugador[1]}, Raza: {jugador[2]}, Nivel: {jugador[3]}")

        nuevo_nombre = input("Ingrese el nuevo nombre de usuario (o presione Enter para no cambiar): ")
        nueva_raza = input("Ingrese la nueva raza preferida (Terran, Zerg, Protoss) (o presione Enter para no cambiar): ")
        nuevo_nivel = input("Ingrese el nuevo nivel de habilidad (Principiante, Intermedio, Avanzado) (o presione Enter para no cambiar): ")

        sql = "UPDATE jugadores SET "
        valores = []
        if nuevo_nombre:
            sql += "nombre = %s, "
            valores.append(nuevo_nombre)
        if nueva_raza:
            sql += "raza = %s, "
            valores.append(nueva_raza)
        if nuevo_nivel:
            sql += "nivel_habilidad = %s, "
            valores.append(nuevo_nivel)

        sql = sql.rstrip(", ") + " WHERE id_jugador = %s"
        valores.append(id_jugador)

        try:
            cursor.execute(sql, tuple(valores))
            self.conexion.commit()
            print("Perfil actualizado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()


    def eliminar(self):
        cursor = self.conexion.cursor()

        print("\n=== ELIMINAR PERFIL DE JUGADOR ===")
        id_jugador = input("Ingrese el ID del jugador que desea eliminar: ")

        cursor.execute("SELECT * FROM jugadores WHERE id_jugador = %s", (id_jugador,))
        jugador = cursor.fetchone()

        if not jugador:
            print("No se encontró un jugador con ese ID.")
            cursor.close()
            return

        print(f"Jugador encontrado: ID: {jugador[0]}, Nombre: {jugador[1]}, Raza: {jugador[2]}, Nivel: {jugador[3]}")
        confirmacion = input("¿Está seguro que desea eliminar este perfil? (S/N): ").strip().upper()

        if confirmacion == "S":
            try:
                cursor.execute("DELETE FROM jugadores WHERE id_jugador = %s", (id_jugador,))
                self.conexion.commit()
                print("Perfil eliminado exitosamente.")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
        else:
            print("Eliminación cancelada.")

        cursor.close()
