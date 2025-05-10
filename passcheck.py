import bcrypt
def pchecker(sqlpassword,password):
    pBytes=password.encode('utf-8')
    sBytes=sqlpassword.encode('utf-8')
    
    if bcrypt.checkpw(pBytes,sBytes):
        return True
    return False
