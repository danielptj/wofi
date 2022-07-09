import psycopg2
import traceback
from DBManager import DBManager
from backend.Cliente import Cliente

class ClienteDAO:

    def listar_todos(self) -> list:
        "retorna todos os clientes"

        cliente_list = []
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute("SELECT id, nome, login, senha, email FROM cliente")

            rows_in_table = cursor.fetchall()
            for row in rows_in_table:
                c = Cliente()
                c.id = row[0]
                c.nome = row[1]
                c.login = row[2]
                c.senha = row[3]
                c.email = row[4]

                cliente_list.append(c)

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return cliente_list


    def listar(self, _id) -> Cliente:
        "retorna UM clinete. Param: cliente.ID"

        cliente = None

        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"SELECT id, nome, login, senha, email FROM cliente WHERE id = {_id}")

            row = cursor.fetchone()

            if row is not None and len(row) > 0:
                cliente = Cliente()
                cliente.id = row[0]
                cliente.nome = row[1]
                cliente.login = row[2]
                cliente.senha = row[3]
                cliente.email = row[4]

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return cliente
    

    def adicionar(self, _nome, _login, _senha, _email) -> bool:
        "Adiciona um novo cliente no banco de dados. params: nome, login, senha e email"

        sucess = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO cliente (nome, login, senha, email) VALUES ('{_nome}', '{_login}', '{_senha}', '{_email}')")
            
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
    

    def atualizar(self,  _nome, _login, _senha, _email, _id) -> bool:
        "Atualiza um cliente no banco de dados. params: nome, login, senha e email"

        sucess = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"UPDATE cliente SET nome = '{_nome}',  login = '{_login}', senha = '{_senha}', email = '{_email}' WHERE id = {_id}")
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
        "Remove um cliente do banco de dados. params: cliente.id"

        sucess = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM cliente WHERE id = {_id}")
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