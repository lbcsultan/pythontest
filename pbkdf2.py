from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256, SHA512
from Crypto.Random import get_random_bytes

# 송신자 
password = b'lskfjglkjsflkhfhjjgjkgdf'
salt = get_random_bytes(16)
keys = PBKDF2(password, salt, 128, count=100000, hmac_hash_module=SHA512)
print(keys.hex()) 
# 송신자 -> 수신자: salt 

# 수신자 
keys = PBKDF2(password, salt, 128, count=100000, hmac_hash_module=SHA512)
print(keys.hex()) 