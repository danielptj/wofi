from backend.DBManager import DBManager
from backend.ProdutoDAO import ProdutoDAO


def _main():
    # cria base para a conexão com o banco de dados 
    DBManager.instance(user="postgres", password="123456", host="localhost", port="5432", database="testeAppDB")

    print("Está vivo!")
    p = ProdutoDAO()

    # r = p.insert_product("Blusa feia", 20.0)
    # print(f"result: {r}" )

    p = p.listar_todos()

    for _p in p:
        print(_p.nome, _p.preco)


if __name__ == "__main__":
    _main()