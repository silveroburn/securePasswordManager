import bcrypt 

# example password 
password = 'sameer'

# converting password to array of bytes 
bytes = password.encode('utf-8') 
print(bytes)

# generating the salt 
salt = bcrypt.gensalt() 

# Hashing the password 
hash = bcrypt.hashpw(bytes, salt) 
print(hash)

