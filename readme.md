# Banco de Dados Nativo do Python

### **Sim**, Python tem um banco de dados **nativo** sem a necessidade de instalar **nada**, e vamos aprender a usar ele.

<br>
<br>

Me chamo **Flaviano**, sou **Desenvolvedor Full-Stack** e estou aqui para te ensinar a usar o **SQLite**. Banco de Dados nativo do Python.
> [Sobre mim](https://github.com/Flaviano-Rodrigues/sobre-mim#sobre-mim)


<br>
<br>

# Iniciando o código:

<br>

Primeiro importe o módulo **sqlite3**:

    import sqlite3 as sl

Aqui chamamos ele de `sl` para facilitar a digitação. Mas você pode chamar de qualquer nome.

<br>
<br>

### Agora vamos criar uma conexão com o banco de dados:

    banco = sl.connect('banco.db')

Aqui criamos uma variável chamada `banco` e usamos o método `connect()` para criar uma conexão com o banco de dados. O método `connect()` recebe como parâmetro o nome do banco de dados, que no caso é `banco.db`. Se o banco de dados não existir, ele será criado.

<br>
<br>

### Banco criado, agora vamos criar uma tabela:
> Tabela é como costumamos chamar as "pastas" do banco de dados.
    
    with banco:
        banco.execute("""
            CREATE TABLE USER (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
        """)

Aqui usamos o método `execute()` para executar o comando SQL. O comando SQL é uma linguagem de consulta estruturada, usada para criar, modificar e extrair dados de um banco de dados relacional. 
<br><br>
Usamos também o `CREATE TABLE USER` para criar uma tabela chamada `USER`. Dentro dos parênteses colocamos os campos da tabela, que no caso são `id`, `name` e `age`. O campo `id` é um campo **único** e **não nulo**, e é **auto incrementado**. O campo `name` é um campo do tipo `TEXT` e o campo `age` é um campo do tipo `INTEGER`.

<br>
<br>

### Agora vamos inserir dados na tabela:

    sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'

    data = [
        (1, 'Flaviano', 18),
        (2, 'Bob', 22),
        (3, 'Chris ', 23)
    ]

    with banco:
        banco.executemany(sql, data)

Atribuímos a variável `sql` o comando SQL para inserir dados na tabela. O `?` é um **placeholder**, que é um espaço reservado para um valor que será inserido posteriormente.
<br><br>
Já a variável `data` é uma lista de tuplas. Cada tupla representa uma linha que será inserida na tabela conténdo os valores que serão inseridos. No caso, a primeira tupla contém os valores `1`, `Flaviano` e `18`, a segunda tupla contém os valores `2`, `Bob` e `22` e a terceira tupla contém os valores `3`, `Chris` e `23`.

<br>
<br>

### Agora vamos selecionar os dados da tabela:

    with banco:
        data = banco.execute('SELECT * FROM USER')
        for linha in data:
            print(linha)


Atribuímos a variavel `data` um execute do banco com o valor `SELECT * FROM USER` para selecionar todos os dados da tabela `USER` e usamos um `for` para percorrer a variável `data` e imprimir cada linha.

<br>
Resultado:

    (1, 'Flaviano', 18)
    (2, 'Bob', 22)
    (3, 'Chris ', 23)


<br>
Comandos SQL Usados Nesse Tutorial:

- O `*` significa que queremos selecionar todos os campos da tabela.
- O `SELECT` é o comando SQL para selecionar dados de uma tabela.
- O `FROM` é o comando SQL para selecionar a tabela que queremos selecionar os dados.


<br>
Outros comandos SQL existentes:

- O `WHERE` é o comando SQL para selecionar os dados que queremos selecionar.
- O `ORDER BY` é o comando SQL para ordenar os dados selecionados.
- O `LIMIT` é o comando SQL para limitar a quantidade de dados selecionados.
- O `HAVING` é usado para especificar uma condição para os dados agrupados.
- O `GROUP BY` é usado para agrupar os dados selecionados.
- O `DISTINCT` é usado para selecionar apenas valores distintos.
- O `AS` é usado para renomear um campo ou tabela.
- O `BETWEEN` é usado para selecionar valores dentro de um intervalo.
- O `IN` é usado para selecionar valores dentro de uma lista.
- O `LIKE` é usado para selecionar valores com base em um padrão.
- O `NOT` é usado para negar uma condição.
- O `OR` é usado para especificar uma condição alternativa.
- O `AND` é usado para especificar múltiplas condições.


<br>
<br>

### **[Veja como ficou o código completo](https://github.com/Flaviano-Rodrigues/Python/blob/master/main.py)**

<br>
<br>

# Conclusão:


Esse foi um tutorial bem simples, mas espero que tenha ajudado você a entender um pouco mais sobre o **SQLite**. Se você tiver alguma dúvida, pode perguntar nos comentários. Se você gostou do tutorial, deixe um like e compartilhe com seus amigos. Até a próxima! :D
