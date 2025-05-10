import bcrypt
def pchecker(sqlpassword,password):
    pBytes=password.encode('utf-8')
    sBytes=sqlpassword.encode('utf-8')
    
    if bcrypt.checkpw(pBytes,sBytes):
        return True
    return False
def convert(password):
    pass_byte=password.encode('utf-8')
    salt=bcrypt.gensalt()
    hash_pass=bcrypt.hashpw(pass_byte,salt)
    return hash_pass