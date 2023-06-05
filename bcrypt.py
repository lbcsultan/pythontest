from base64 import b64encode 
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import bcrypt, bcrypt_check

# 사용자 등록: 패스워드 해시 생성, 등록 
password = b'dskflsdkjakjfl'
b64pwd = b64encode(SHA256.new(password).digest())
bcrypt_hash = bcrypt(b64pwd, 12) 
print("Password: {0}".format(password) ) 
print("b64Password", b64pwd)
print('Password hash: {0}'.format(bcrypt_hash))

# 로그인: 패스워드 검증 
# password1 = password
password1 = b'lsldkjfsdjflsk' 
try: 
    b64pwd1 = b64encode(SHA256.new(password1).digest())
    result = bcrypt_check(b64pwd1, bcrypt_hash)
    # print(result)
except ValueError:
    print("Icorrect password!")