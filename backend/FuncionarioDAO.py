import psycopg2
import traceback
from backend.DBManager import DBManager
from backend.Funcionario import Funcionario

class FuncionarioDAO:

    def listar_todos(self) -> list:
        "retorna todos os funcionarios"

        funcionario_list = []
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute("SELECT id, nome, login, senha, email FROM funcionario")

            rows_in_table = cursor.fetchall()
            for row in rows_in_table:
                f = Funcionario()
                f.id = row[0]
                f.nome = row[1]
                f.login = row[2]
                f.senha = row[3]
                f.email = row[4]

                funcionario_list.append(f)

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return funcionario_list


    def listar(self, _id) -> Funcionario:
        "retorna UM funcionario. params: funcionario.ID"

        funcionario = None

        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"SELECT id, nome, login, senha, email FROM funcionario WHERE id = {_id}")

            row = cursor.fetchone()

            if row is not None and len(row) > 0:
                funcionario = Funcionario()
                funcionario.id = row[0]
                funcionario.nome = row[1]
                funcionario.login = row[2]
                funcionario.senha = row[3]
                funcionario.email = row[4]

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return funcionario
    

    def adicionar(self, _nome, _login, _senha, _email) -> bool:
        "Adiciona um novo funcionario no banco de dados. params: nome, login, senha e email"

        success = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO funcionario (nome, login, senha, email) VALUES ('{_nome}', '{_login}', '{_senha}', '{_email}')")
            
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
    

    def atualizar(self,  _nome, _login, _senha, _email, _id) -> bool:
        "Atualiza um funcionario no banco de dados. params: nome, login, senha e email"

        success = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"UPDATE funcionario SET nome = '{_nome}',  login = '{_login}', senha = '{_senha}', email = '{_email}' WHERE id = {_id}")
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
        "Remove um funcionario do banco de dados. params: funcionario.id"

        success = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM funcionario WHERE id = {_id}")
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