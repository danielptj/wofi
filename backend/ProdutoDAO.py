import psycopg2
import traceback
from backend.Produto import Produto
from backend.DBManager import DBManager

class ProdutoDAO(object):

    def listar_todos(self) -> list:
        "retorna todos os produtos no banco de dados"

        produto_list = []
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute("SELECT id, nome, preco FROM produto")

            rows_in_table = cursor.fetchall()
            for row in rows_in_table:
                p = Produto()
                p.id = row[0]
                p.nome = row[1]
                p.preco = row[2]

                produto_list.append(p)

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return produto_list


    def listar(self, _id) -> Produto:
        "retorna um produto. param = produto.ID"

        produto = None

        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"SELECT id, nome, preco FROM produto WHERE id = {_id}")

            row = cursor.fetchone()

            if row is not None and len(row) > 0:
                produto = Produto()
                produto.id = row[0]
                produto.nome = row[1]
                produto.preco = row[2]

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return produto
    

    def adicionar(self, _nome, _preco) -> bool:
        "Adiciona um novo produto no banco de dados. passing nome and preco"

        sucess = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO produto (nome, preco) VALUES ('{_nome}', {_preco})")
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
    

    def atualizar(self, _nome, _preco, _id) -> bool:
        "Atualiza produto do banco de dados. passing nome, preco and id"

        sucess = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"UPDATE produto SET nome = '{_nome}', preco = {_preco} WHERE id = {_id}")
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
        "Remove produto do banco de dados. passing produto.id"

        sucess = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM produto WHERE id = {_id}")
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