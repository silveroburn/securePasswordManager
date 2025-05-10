import bcrypt
def pchecker(sqlpassword,password):
    bytes=password.encode('utf-8')
    if bcrypt.checkpw(bytes,sqlpassword):
        return True
    return False
