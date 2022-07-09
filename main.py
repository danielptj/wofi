from backend.DBManager import DBManager
from backend.ProdutoDAO import ProductDAO


def _main():
    # cria base para a conexão com o banco de dados 
    DBManager.instance(user="postgres", password="123456", host="localhost", port="5432", database="testeAppDB")

    print("Está vivo!")
    # p = ProductDAO()

    # r = p.insert_product("Blusa feia", 20.0)
    # print(f"result: {r}" )

    # pl = p.get_all_products()

    # for _p in pl:
    #     print(_p.name, _p.price)


if __name__ == "__main__":
    _main()