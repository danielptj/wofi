import psycopg2
import traceback
from backend.DBManager import DBManager
from backend.Estoque import Estoque

class EstoqueDAO:

    def listar_todos(self) -> list:
        "return all products<ID> and quantity in estoque table"

        estoque_list = []
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute("SELECT id, funcionario_id FROM estoque")

            rows_in_table = cursor.fetchall()
            for row in rows_in_table:
                e = Estoque()
                e.id = row[0]
                e.funcionario_id = row[1]

                estoque_list.append(e)

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return estoque_list

    def listar(self, _id) -> Estoque:
        "retorna UM estoque. Param: estoque.ID"

        estoque = None

        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"SELECT id, funcionario_id FROM estoque WHERE id = {_id}")

            row = cursor.fetchone()

            if row is not None and len(row) > 0:
                estoque = Estoque()
                estoque.id = row[0]
                estoque.funcionario_id = row[1]

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return estoque
    

    def adicionar(self, _funcionario_id) -> bool:
        "Add a new product in database. passing name and price"

        sucess = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO estoque (funcionario_id) VALUES ({_funcionario_id})")
            connection.commit()
            if cursor.rowcount == 1:
                sucess = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucess
    

    def atualizar(self, _funcionario_id, _id) -> bool:
        "Update a estoque in the database, passing name, price and id"

        sucess = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"UPDATE estoque SET funcionario_id = {_funcionario_id} WHERE id = {_id}")
            connection.commit()
            if cursor.rowcount == 1:
                sucess = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucess


    def remover(self, _id) -> bool:
        "Remove estoque. param = estoque.id"

        sucess = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM estoque WHERE id = {_id}")
            connection.commit()
            if cursor.rowcount == 1:
                sucess = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucess