import pymysql as con
import passcheck

connection = con.connect(
    host='metro.proxy.rlwy.net',
    port=37344,
    user='root',
    password='shPJpgLpflJugfajAbJncpImimwPOrKS',
    database='railway'
)

print('is connected now')

cursor = connection.cursor()

def signup(username, password, email):
    if (password == None):
        print("Password required")
        return -2
    elif (username == None):
        print("username required")
        return -2
    elif (email == None):
        print("Email required")
        return -2
    cursor.execute('select * from users where username = %s', username)
    row = cursor.fetchall() 
    if (len(row) == 1):
        print("Username already exists")
        return -1
    
def chkuser(username, email):
    cursor.execute('select * from users where username = %s' , (username,))
    rows = cursor.fetchall()
    if (len(rows) >= 1):
        return "Username already exists"
    
    cursor.execute('select * from users where email = %s', (email,))
    rows = cursor.fetchall()
    if (len(rows) >= 1):
        return "Email already in use"
    
def addUser(username, email, password):
    message = chkuser(username, email)
    if message != None:
        return message
    newPass = convert(password)
    cursor.execute('insert into users values (%s, %s, %s, %s, %s)', (username, newPass, 0, 0, email))
    connection.commit()
    return "User created successfully"
    
def get_email(username):
    cursor.execute('select * from users where username = %s', username)
    rows = cursor.fetchall()
    if (len(rows) == 1):
        return rows[0][4]
    else:
        return 'No user found'

def checker(username, curPassword):
    cursor.execute('select * from users where username = %s', (username))
    row = cursor.fetchall()
    # print(row)
    if (len(row) == 0):
        print("no such username")
        return -1
    if (row[0][2] == 5):
        print("banned")
        cursor.execute('update users set valid = 1 where username = %s', username)
        connection.commit()
        return -2
    hashPassword = row[0][1]
    if passcheck.pchecker(hashPassword, curPassword):
        print("login successfull")
        cursor.execute('update users set counter = 0 where username = %s', username)
        connection.commit()
        return 0
    else:
        cursor.execute('select * from users where username = %s', username)
        info = cursor.fetchall()
        counterValue = info[0][2]
        cursor.execute('update users set counter = %s where username = %s', (counterValue + 1, username))
        connection.commit()
        if (5 - (counterValue + 1) == 0):
            print("banned: 0 tries left")
            cursor.execute('update users set valid = 1 where username = %s', username)
            connection.commit()
            return -2
        else:
            print(5 - (counterValue + 1), " tries left")
            return counterValue + 1
                   
get_email('sameer')
# print(connection)
# print(checker("sameer", "sameer"))
    