import psycopg2
import traceback
from backend.DBManager import DBManager
from backend.Pedido import Pedido

class PedidoDAO:

    def listar_todos(self) -> list:

        pedido_list = []
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute("SELECT id, funcionario_id, cliente_id FROM pedido")

            rows_in_table = cursor.fetchall()
            for row in rows_in_table:
                p = Pedido()
                p.id = row[0]
                p.funcionario_id = row[1]
                p.cliente_id = row[2]

                pedido_list.append(p)

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return pedido_list

    def listar(self, _id) -> Pedido:
        "retorna UM pedido. Param: pedido.ID"

        pedido = None

        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"SELECT id, funcionario_id, cliente_id FROM pedido WHERE id = {_id}")

            row = cursor.fetchone()

            if row is not None and len(row) > 0:
                pedido = Pedido()
                pedido.id = row[0]
                pedido.funcionario_id = row[1]
                pedido.cliente_id = row[2]

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return pedido

    
    def adicionar(self, _funcionario_id, _cliente_id) -> bool:
        "Adiciona um novo pedido no banco de dados. params: funcionario_id e cliente_id"

        success = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO pedido (funcionario_id, cliente_id) VALUES ({_funcionario_id}, {_cliente_id})")
            
            connection.commit()

            if cursor.rowcount == 1:
                success = True

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return success


    def atualizar(self,  _funcionario_id, _cliente_id, _id) -> bool:
        "Atualiza um pedido no banco de dados. params: funcionario_id e cliente_id"

        success = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"UPDATE pedido SET funcionario_id = {_funcionario_id}, cliente_id = {_cliente_id} WHERE id = {_id}")
            connection.commit()
            if cursor.rowcount == 1:
                success = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return success

    def remover(self, _id) -> bool:
        "Remove um pedido do banco de dados. params: pedido.id"

        success = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM pedido WHERE id = {_id}")
            connection.commit()
            if cursor.rowcount == 1:
                success = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return success