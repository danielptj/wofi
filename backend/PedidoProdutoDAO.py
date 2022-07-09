import psycopg2
import traceback
from DBManager import DBManager
from backend.PedidoProduto import PedidoProduto

class PedidoProdutoDAO:

    def listar_todos(self) -> list:
        "retorna todos os pedido_produtos"

        pedido_produto_list = []
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute("SELECT pedido_id, produto_id, quantidade FROM pedido_produto")

            rows_in_table = cursor.fetchall()
            for row in rows_in_table:
                pp = PedidoProduto()
                pp.pedido_id = row[0]
                pp.produto_id = row[1]
                pp.quantidade = row[2]

                pedido_produto_list.append(pp)

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return pedido_produto_list


    def listar(self, _pedido_id, _produto_id) -> PedidoProduto:
        "retorna uma linha de pedido_produto. Param: pedido_id e produto_id"

        pedido_produto = None

        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"SELECT pedido_id, produto_id, quantidade FROM pedido_produto WHERE pedido_id  = {_pedido_id } AND produto_id = {_produto_id}")

            row = cursor.fetchone()

            if row is not None and len(row) > 0:
                pedido_produto = PedidoProduto()
                pedido_produto.pedido_id = row[0]
                pedido_produto.produto_id = row[1]
                pedido_produto.quantidade = row[2]


        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return pedido_produto
    

    def adicionar(self, _pedido_id, _produto_id, _quantidade) -> bool:
        "Adiciona um novo pedido_produto no banco de dados. params: pedido_id, produto_id e quantidade"

        sucess = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO pedido_produto ( pedido_id, produto_id, quantidade) VALUES ({_pedido_id}, {_produto_id}, {_quantidade})")
            
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
    

    def atualizar(self, _pedido_id, _produto_id, _quantidade) -> bool:
        "Atualiza a quantidade de produtos de um estoque no banco de dados. params: estoque.id, produto.id e quantidade"

        sucess = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"UPDATE pedido_produto SET quantidade = {_quantidade} WHERE pedido_id  = {_pedido_id } AND produto_id = {_produto_id}")
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


    def remover(self,  _pedido_id, _produto_id) -> bool:
        "Remove um produto em um pedido. params: pedido.id e produto.id"

        sucess = False
        try:
            connection = DBManager.connect_with_database()

            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM pedido_produto WHERE pedido_id = {_pedido_id} AND produto_id = {_produto_id}")
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