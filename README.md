# wofi

Aplicação para o trabalho final de Banco de Dados 1

## 🐺 Equipe wofi

- Daniel Fonseca Pantoja
- Guilherme Gomes Cayres
- Mauro Victor Pimentel Dias
- Nicolas Barbosa Cavalcante
- José Carlos Wolff
- Paulo Henrique Gomes

## Sobre a aplicação

O **wofi** é uma aplicação CLI que faz acesso ao banco de dados
para realizar algumas operações, simulando um sistema de uma
loja, gerenciando **clientes**, **funcionários**, **estoque**, **produtos** e **pedidos**.

## 💻 Usando a aplicação

Para usar a aplicação, siga os passos:

1. Clone o repositório:
    ```
    git clone https://github.com/paulohgs/wofi
    ```

2. Instale as dependências:
    ```
    pip install psycopg2
    ```
    ```
    pip install colorama
    ```
    
3. Importe o esquema SQL

4. Conecte o banco com a aplicação:

    Na função main do arquivo command_line_interface.py é necessário mudar os paramentros do método DBManager.instance
    ```
    DBManager.instance(user="postgres", password=senha, host="localhost", port=porta, database=nome_da_database)
    ```
    Dessa forma, a conexão com o banco de dados vai ser estabelecida globalmente na aplicação.

5. Inicie a aplicação pelo terminal:
    ```
    {local de instalação do python}\python.exe {caminho do arquivo}\command_line_interface.py
    ```
6. Pronto!

[⬆ Voltar ao topo](#wofi)
