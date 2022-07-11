import os
from colorama import init, Fore, Back, Style
from backend.DBManager import DBManager
from backend.ClienteDAO import ClienteDAO 
from backend.EstoqueDAO import EstoqueDAO 
from backend.EstoqueProdutoDAO import EstoqueProdutoDAO 
from backend.FuncionarioDAO import FuncionarioDAO
from backend.PedidoDAO import PedidoDAO 
from backend.PedidoProdutoDAO import PedidoProdutoDAO 
from backend.ProdutoDAO import ProdutoDAO 

def main():
    # mudar os valores de acordo com o seu banco de dados
    DBManager.instance(user="postgres", password="2714", host="localhost", port="5432", database="testeAppDB")
    init()
    print_main_menu()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def print_header(text):
    cls()
    print(Style.BRIGHT + '\n--------------------------------------------------'
          + '------------------------------')
    print('                                  ' + text)
    print('-------------------------------------------------------------------'
          + '-------------\n' + Style.RESET_ALL)

def print_main_menu():
    while True:
        print_header('wofi')
        print('1. Gerenciar' + Fore.CYAN + ' clientes\n' + Style.RESET_ALL)
        print('2. Gerenciar' + Fore.CYAN + ' funcionários\n' + Style.RESET_ALL)
        print('3. Gerenciar' + Fore.CYAN + ' estoque\n' + Style.RESET_ALL)
        print('4. Gerenciar' + Fore.CYAN + ' produtos no estoque\n' + Style.RESET_ALL)
        print('5. Gerenciar' + Fore.CYAN + ' produtos\n' + Style.RESET_ALL)
        print('6. Gerenciar' + Fore.CYAN + ' pedidos\n' + Style.RESET_ALL)
        print('7. Gerenciar' + Fore.CYAN + ' produtos em pedidos\n' + Style.RESET_ALL)
        print('0. ' + Fore.RED + 'Sair\n' + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.CYAN + 'Escolha uma opção: ' + Style.RESET_ALL)
        value = input()
        if value == '1':
            print_customer_menu()
        elif value == '2':
            print_employee_menu()
        elif value == '3':
            print_stock_menu()
        elif value == '4':
            print_stock_product_menu()
        elif value == '5':
            print_products_menu()
        elif value == '6':
            print_orders_menu()
        elif value == '7':
            print_order_products_menu()
        elif value == '0':
            break
        else:
            print(Style.BRIGHT + Fore.RED + '\ninput inválido!' + Style.RESET_ALL)
            input()    
        
def print_customer_menu():
    while True:
        c = ClienteDAO()
        print_header('GERENCIAR CLIENTES')
        print('1. Listar clientes\n')
        print('2. Procurar um cliente\n')
        print('3. Adicionar um cliente\n')
        print('4. Atualizar um cliente\n')
        print('5. Remover um cliente\n')
        print('0. ' + Fore.RED + 'Voltar\n' + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.CYAN + 'Escolha uma opção: ' + Style.RESET_ALL)
        value = input()
        if value == '1':
            lista = c.listar_todos()
            for _c in lista:
                print(_c.id,'. ', _c.nome, ', ', _c.login, ', ', _c.senha, ', ', _c.email)
            input()
        elif value == '2':
            _id = input('ID do cliente: ')
            _c = c.listar(_id)
            if (_c):
                print('Cliente de ID', _c.id, ': ', _c.nome, ', ', _c.login, ', ', _c.senha, ', ', _c.email)
            else:
                print('ID inválido!')
            input()
        elif value == '3':
            _nome = input('Nome cliente: ')
            _login = input('Login cliente: ')
            _senha = input('Senha cliente: ')
            _email = input('Email cliente: ')
            a = c.adicionar(_nome, _login, _senha, _email)
            if (a):
                print(f'Adicionado com sucesso')
            else:
                print('Erro ao adicionar')   
            input()
        elif value == '4':
            _nome = input('Atualizar nome cliente: ')
            _login = input('Atualizar login cliente: ')
            _senha = input('Atualizar senha cliente: ')
            _email = input('Atualizar email cliente: ')
            _id = input('ID do cliente a ser atualizado: ')
            a = c.atualizar(_nome, _login, _senha, _email, _id)
            if (a):
                print(f'Atualizado com sucesso')
            else:
                print('Erro ao atualizar')   
            input()
        elif value == '5':
            _id = input('ID do cliente a ser removido: ')
            a = c.remover(_id)
            if (a):
                print(f'Removido com sucesso')
            else:
                print('ID inválido!')   
            input()
        elif value == '0':
            break
        else:
            print(Style.BRIGHT + Fore.RED + '\ninput inválido!' + Style.RESET_ALL)
            input()

def print_employee_menu():
    while True:
        f = FuncionarioDAO()
        print_header('GERENCIAR FUNCIONÁRIOS')
        print('1. Listar funcionários\n')
        print('2. Procurar um funcionário\n')
        print('3. Adicionar um funcionário\n')
        print('4. Atualizar um funcionário\n')
        print('5. Remover um funcionário\n')
        print('0. ' + Fore.RED + 'Voltar\n' + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.CYAN + 'Escolha uma opção: ' + Style.RESET_ALL)
        value = input()
        if value == '1':
            lista = f.listar_todos()
            for _f in lista:
                print(_f.id,'. ', _f.nome, ', ', _f.login, ', ', _f.senha, ', ', _f.email)
            input()
        elif value == '2':
            _id = input('ID do funcionário: ')
            _f = f.listar(_id)
            if (_f):
                print('Funcionário de ID', _f.id, ': ', _f.nome, ', ', _f.login, ', ', _f.senha, ', ', _f.email)
            else:
                print('ID inválido!')
            input()
        elif value == '3':
            _nome = input('Nome funcionário: ')
            _login = input('Login funcionário: ')
            _senha = input('Senha funcionário: ')
            _email = input('Email funcionário: ')
            a = f.adicionar(_nome, _login, _senha, _email)
            if (a):
                print(f'Adicionado com sucesso')
            else:
                print('Erro ao adicionar')   
            input()
        elif value == '4':
            _nome = input('Atualizar nome funcionário: ')
            _login = input('Atualizar login funcionário: ')
            _senha = input('Atualizar senha funcionário: ')
            _email = input('Atualizar email funcionário: ')
            _id = input('ID do funcionário a ser atualizado: ')
            a = f.atualizar(_nome, _login, _senha, _email, _id)
            if (a):
                print(f'Atualizado com sucesso')
            else:
                print('Erro ao atualizar')   
            input()
        elif value == '5':
            _id = input('ID do funcionário a ser removido: ')
            a = f.remover(_id)
            if (a):
                print(f'Removido com sucesso')
            else:
                print('ID inválido!')   
            input()
        elif value == '0':
            break
        else:
            print(Style.BRIGHT + Fore.RED + '\ninput inválido!' + Style.RESET_ALL)
            input()

def print_stock_menu():
    while True:
        e = EstoqueDAO()
        print_header('GERENCIAR ESTOQUE')
        print('1. Listar todos os produtos no estoque\n')
        print('2. Retorna UM estoque\n')
        print('3. Adicionar ao estoque\n')
        print('4. Atualizar estoque\n')
        print('5. Remover estoque\n')
        print('0. ' + Fore.RED + 'Voltar\n' + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.CYAN + 'Escolha uma opção: ' + Style.RESET_ALL)
        value = input()
        if value == '1':
            lista = e.listar_todos()
            for _e in lista:
                print(_e.id,'. ', _e.nome, ', ', _e.login, ', ', _e.senha, ', ', _e.email)
            input()
        elif value == '2':
            _id = input('ID do estoque: ')
            _e = e.listar(_id)
            if (_e):
                print('estoque de ID', _e.id, ': ', _e.nome, ', ', _e.login, ', ', _e.senha, ', ', _e.email)
            else:
                print('ID inválido!')
            input()
        elif value == '3':
            _funcionario_id = input('ID do funcionário do estoque: ')
            a = e.adicionar(_funcionario_id)
            if (a):
                print(f'Adicionado com sucesso')
            else:
                print('Erro ao adicionar')   
            input()
        elif value == '4':
            _funcionario_id = input('Atualizar ID do funcionário do estoque: ')
            _id = input('ID do estoque a ser atualizado: ')
            a = e.atualizar(_funcionario_id, _id)
            if (a):
                print(f'Atualizado com sucesso')
            else:
                print('Erro ao atualizar')   
            input()
        elif value == '5':
            _id = input('ID do estoque a ser removido: ')
            a = e.remover(_id)
            if (a):
                print(f'Removido com sucesso')
            else:
                print('ID inválido!')   
            input()
        elif value == '0':
            break
        else:
            print(Style.BRIGHT + Fore.RED + '\ninput inválido!' + Style.RESET_ALL)
            input()

def print_stock_product_menu():
    while True:
        ep = EstoqueProdutoDAO()
        e = EstoqueDAO()
        p = ProdutoDAO()
        print_header('GERENCIAR ESTOQUE_PRODUTO')
        print('1. Listar todos os estoque_produtos\n')
        print('2. Procura um estoque_produto\n')
        print('3. Adicionar um novo estoque_produto\n')
        print('4. Atualiza a quantidade de produtos de um estoque\n')
        print('5. Remover produto no estoque\n')
        print('0. ' + Fore.RED + 'Voltar\n' + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.CYAN + 'Escolha uma opção: ' + Style.RESET_ALL)
        value = input()
        if value == '1':
            lista = ep.listar_todos()
            for _ep in lista:
                print('IDs: ', _ep.estoque_id, ', ', _ep.produto_id, 'Quantidade: ', _ep.quantidade)
            input()
        elif value == '2':
            _eid = input('ID do estoque: ')
            _pid = input('ID do produto: ')
            _e = e.listar(_eid)
            _p = p.listar(_pid)
            if (_e) and (_p):
                _ep = ep.listar(_eid, _pid)
                if (_ep): 
                    print('IDs:', _ep.estoque_id, ', ', _ep.produto_id, 'Quantidade: ', _ep.quantidade)
                else:
                    print('IDs inválidos!')
            else:
                print('IDs inválidos!')
            input()
        elif value == '3':
            while True:
                _eid = input('ID do estoque: ')
                if (e.listar(_eid)):
                    break
                else:
                    print('ID do estoque inválido')
                input()
            while True:
                _pid = input('ID do produto: ')
                if (p.listar(_pid)):
                    break
                else:
                    print('ID do produto inválido')
                input()
            _quantidade = input('Quantidade de produtos: ')
            a = ep.adicionar(_eid, _pid, _quantidade)
            if (a):
                print(f'Adicionado com sucesso')
            else:
                print('Erro ao adicionar')   
            input()
        elif value == '4':
            while True:
                _eid = input('ID do estoque a ser atualizado: ')
                if (e.listar(_eid)):
                    break
                else:
                    print('ID do estoque inválido')
                input()
            while True:
                _pid = input('ID do produto a ser atualizado: ')
                if (p.listar(_pid)):
                    break
                else:
                    print('ID do produto inválido')
                input()
            _quantidade = input('Atualizar quantidade de produtos: ')
            a = ep.atualizar(_eid, _pid, _quantidade)
            if (a):
                print(f'Atualizado com sucesso')
            else:
                print('Erro ao atualizar')   
            input()
        elif value == '5':
            while True:
                _eid = input('ID do estoque: ')
                if (e.listar(_eid)):
                    break
                else:
                    print('ID do estoque inválido')
                input()
            while True:
                _pid = input('ID do produto: ')
                if (p.listar(_pid)):
                    break
                else:
                    print('ID do produto inválido')
                input()
            a = ep.remover(_eid, _pid)
            if (a):
                print(f'Removido com sucesso')
            else:
                print('Erro ao remover')   
            input()
        elif value == '0':
            break
        else:
            print(Style.BRIGHT + Fore.RED + '\ninput inválido!' + Style.RESET_ALL)
            input()

def print_products_menu():
    while True:
        p = ProdutoDAO()
        print_header('GERENCIAR PRODUTOS')
        print('1. Listar produtos\n')
        print('2. Procurar um produto\n')
        print('3. Adicionar um produto\n')
        print('4. Atualizar um produto\n')
        print('5. Remover um produto\n')
        print('0. ' + Fore.RED + 'Voltar\n' + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.CYAN + 'Escolha uma opção: ' + Style.RESET_ALL)
        value = input()
        if value == '1':
            lista = p.listar_todos()
            for _p in lista:
                print(_p.id,'. ', _p.nome, ', ', _p.preco)
            input()
        elif value == '2':
            _id = input('ID do produto: ')
            _p = p.listar(_id)
            if (_p):
                print('produto de ID', _p.id, ': ', _p.nome, ', ', _p.preco)
            else:
                print('ID inválido!')
            input()
        elif value == '3':
            _nome = input('Nome produto: ')
            _preco = input('Preço produto: ')
            a = p.adicionar(_nome, _preco)
            if (a):
                print(f'Adicionado com sucesso')
            else:
                print('Erro ao adicionar')   
            input()
        elif value == '4':
            _nome = input('Atualizar nome do produto: ')
            _preco = input('Atualizar preço do produto: ')
            _id = input('ID do produto a ser atualizado: ')
            a = p.atualizar(_nome, _preco, _id)
            if (a):
                print(f'Atualizado com sucesso')
            else:
                print('Erro ao atualizar')   
            input()
        elif value == '5':
            _id = input('ID do produto a ser removido: ')
            a = p.remover(_id)
            if (a):
                print(f'Removido com sucesso')
            else:
                print('ID inválido!')   
            input()
        elif value == '0':
            break
        else:
            print(Style.BRIGHT + Fore.RED + '\ninput inválido!' + Style.RESET_ALL)
            input()

def print_orders_menu():
    while True:
        pe = PedidoDAO()
        f = FuncionarioDAO()
        c = ClienteDAO()
        print_header('GERENCIAR PEDIDOS')
        print('1. Listar pedidos\n')
        print('2. Procurar um pedido\n')
        print('3. Adicionar um pedido\n')
        print('4. Atualizar um pedido\n')
        print('5. Remover um pedido\n')
        print('0. ' + Fore.RED + 'Voltar\n' + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.CYAN + 'Escolha uma opção: ' + Style.RESET_ALL)
        value = input()
        if value == '1':
            lista = pe.listar_todos()
            for _pe in lista:
                print(_pe.id,'. ', _pe.funcionario_id, ', ', _pe.cliente_id)
            input()
        elif value == '2':
            _id = input('ID do pedido: ')
            _pe = pe.listar(_id)
            if (_pe):
                print('Pedido de ID', _pe.id, ': ', _pe.funcionario_id, ', ', _pe.cliente_id)
            else:
                print('ID inválido!')
            input()
        elif value == '3':
            while True:
                _fid = input('ID do funcionário: ')
                if (f.listar(_fid)):
                    break
                else:
                    print('ID do funcionário inválido')
                    input()
            while True:
                _cid = input('ID do cliente: ')
                if (c.listar(_cid)):
                    break
                else:
                    print('ID do cliente inválido')
                    input()
            a = pe.adicionar(_fid, _cid)
            if (a):
                print(f'Adicionado com sucesso')
            else:
                print('Erro ao adicionar')   
            input()
        elif value == '4':
            while True:
                _fid = input('Atualizar ID do funcionário: ')
                if (f.listar(_fid)):
                    break
                else:
                    print('ID do funcionário inválido')
                    input()
            while True:
                _cid = input('Atualizar ID do cliente: ')
                if (c.listar(_cid)):
                    break
                else:
                    print('ID do cliente inválido')
                    input()
            while True:
                _id = input('ID do pedido a ser atualizado: ')
                if (c.listar(_id)):
                    break
                else:
                    print('ID do cliente inválido')
                    input()
            a = pe.atualizar(_fid, _cid, _id)
            if (a):
                print(f'Atualizado com sucesso')
            else:
                print('Erro ao atualizar')   
            input()
        elif value == '5':
            _id = input('ID do pedido a ser removido: ')
            a = pe.remover(_id)
            if (a):
                print(f'Removido com sucesso')
            else:
                print('ID inválido!')   
            input()
        elif value == '0':
            break
        else:
            print(Style.BRIGHT + Fore.RED + '\ninput inválido!' + Style.RESET_ALL)
            input()

def print_order_products_menu():
    while True:
        pep = PedidoProdutoDAO()
        pe = PedidoDAO()
        p = ProdutoDAO()
        print_header('GERENCIAR PRODUTOS EM PEDIDOS')
        print('1. Listar produtos em pedidos\n')
        print('2. Procurar um produto de um pedido\n')
        print('3. Adicionar um produto a um pedido\n')
        print('4. Atualizar um produto de um pedido\n')
        print('5. Remover um produto de um pedido\n')
        print('0. ' + Fore.RED + 'Voltar\n' + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.CYAN + 'Escolha uma opção: ' + Style.RESET_ALL)
        value = input()
        if value == '1':
            lista = pep.listar_todos()
            for _pep in lista:
                print('IDs: ', _pep.pedido_id, ', ', _pep.produto_id, 'Quantidade: ', _pep.quantidade)
            input()
        elif value == '2':
            _peid = input('ID do pedido: ')
            _pid = input('ID do produto: ')
            _e = pe.listar(_peid)
            _p = p.listar(_pid)
            if (_e) and (_p):
                _pep = pep.listar(_peid, _pid)
                if (_pep): 
                    print('IDs:', _pep.pedido_id, ', ', _pep.produto_id, 'Quantidade: ', _pep.quantidade)
                else:
                    print('IDs inválidos!')
            else:
                print('IDs inválidos!')
            input()
        elif value == '3':
            while True:
                _peid = input('ID do pedido: ')
                if (pe.listar(_peid)):
                    while True:
                        _pid = input('ID do produto: ')
                        if (p.listar(_pid)):
                            _quantidade = input('Quantidade de produtos: ')
                            a = pep.adicionar(_peid, _pid, _quantidade)
                            if (a):
                                print(f'Adicionado com sucesso')
                            else:
                                print('Erro ao adicionar')   
                        else:
                            print('ID do produto inválido')
                else:
                    print('ID do pedido inválido')
                input()
                break
        elif value == '4':
            while True:
                _peid = input('ID do pedido a ser atualizado: ')
                if (pe.listar(_peid)):
                    break
                else:
                    print('ID do pedido inválido')
                input()
            while True:
                _pid = input('ID do produto a ser atualizado: ')
                if (p.listar(_pid)):
                    break
                else:
                    print('ID do produto inválido')
                input()
            _quantidade = input('Atualizar quantidade de produtos: ')
            a = pep.atualizar(_peid, _pid, _quantidade)
            if (a):
                print(f'Atualizado com sucesso')
            else:
                print('Erro ao atualizar')   
            input()
        elif value == '5':
            while True:
                _peid = input('ID do pedido: ')
                if (pe.listar(_peid)):
                    break
                else:
                    print('ID do pedido inválido')
                input()
            while True:
                _pid = input('ID do produto: ')
                if (p.listar(_pid)):
                    break
                else:
                    print('ID do produto inválido')
                input()
            a = pep.remover(_peid, _pid)
            if (a):
                print(f'Removido com sucesso')
            else:
                print('Erro ao remover')   
            input()
        elif value == '0':
            break
        else:
            print(Style.BRIGHT + Fore.RED + '\ninput inválido!' + Style.RESET_ALL)
            input()

if __name__ == '__main__':
    main()
