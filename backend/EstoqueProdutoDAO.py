import psycopg2
import traceback
from backend.DBManager import DBManager
from backend.EstoqueProduto import EstoqueProduto

class EstoqueProdutoDAO:

    def listar_todos(self) -> list:
        "retorna todos os estoque_produtos"

        estoque_produto_list = []
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute("SELECT estoque_id, produto_id, quantidade FROM estoque_produto")

            rows_in_table = cursor.fetchall()
            for row in rows_in_table:
                ep = EstoqueProduto()
                ep.estoque_id = row[0]
                ep.produto_id = row[1]
                ep.quantidade = row[2]

                estoque_produto_list.append(ep)

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return estoque_produto_list


    def listar(self, _estoque_id, _produto_id) -> EstoqueProduto:
        "retorna uma linha de estoque_produto. Param: estoque_id e produto_id"

        estoque_produto = None

        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"SELECT estoque_id, produto_id, quantidade FROM estoque_produto WHERE estoque_id  = {_estoque_id } AND produto_id = {_produto_id}")

            row = cursor.fetchone()

            if row is not None and len(row) > 0:
                estoque_produto = EstoqueProduto()
                estoque_produto.estoque_id = row[0]
                estoque_produto.produto_id = row[1]
                estoque_produto.quantidade = row[2]


        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return estoque_produto
    

    def adicionar(self, _estoque_id, _produto_id, _quantidade) -> bool:
        "Adiciona um novo estoque_produto no banco de dados. params: estoque_id, produto_id e quantidade"

        success = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO estoque_produto ( estoque_id, produto_id, quantidade) VALUES ({_estoque_id}, {_produto_id}, {_quantidade})")
            
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
    

    def atualizar(self, _estoque_id, _produto_id, _quantidade) -> bool:
        "Atualiza a quantidade de produtos de um estoque no banco de dados. params: estoque.id, produto.id e quantidade"

        success = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"UPDATE estoque_produto SET quantidade = {_quantidade} WHERE estoque_id  = {_estoque_id } AND produto_id = {_produto_id}")
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


    def remover(self,  _estoque_id, _produto_id) -> bool:
        "Remove um produto em um estoque. params: estoque.id e produto.id"

        success = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM estoque_produto WHERE estoque_id = {_estoque_id} AND produto_id = {_produto_id}")
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