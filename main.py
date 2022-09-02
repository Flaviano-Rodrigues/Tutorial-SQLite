import sqlite3 as sl

banco = sl.connect('test.db')


def criandoTabela():
    with banco:
        banco.execute("""
            CREATE TABLE USER (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
        """)


def adicionadoItem():
    sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'

    data = [
        (1, 'Flaviano', 18),
        (2, 'Bob', 22),
        (3, 'Chris ', 23)
    ]

    with banco:
        banco.executemany(sql, data)


def vendoDaTabela():
    with banco:
        data = banco.execute('SELECT * FROM USER')
        for row in data:
            print(row)


criandoTabela()
adicionadoItem()
vendoDaTabela()
