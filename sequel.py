import pymysql as con

connection = con.connect(
    host='metro.proxy.rlwy.net',
    port=37344,
    user='root',
    password='shPJpgLpflJugfajAbJncpImimwPOrKS',
    database='railway'
)

print('is connected now')

cursor = connection.cursor()


# comm = "insert into users (username, hashPassword, counter) values ('sameer', 'something password', 1)"
# cursor.execute(comm)
# connection.commit()
# cursor.execute('update users set email = "sameer2020sameer123@gmail.com" where username = "sameer"')
# connection.commit()
# row = cursor.fetchall()

def checker(username, password):
    cursor.execute('select * from users where username = %s', (username))
    row = cursor.fetchall()
    print(row)

print(connection)
checker("sameer", "something password")
    
print('hello world')