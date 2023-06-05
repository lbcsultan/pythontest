import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes 

# 송신자가 암호화 
data = "secret 한글.......secret 한글.......".encode('utf8')
key = get_random_bytes(32)  # 128: 16, 192: 24, 256: 32
cipher = AES.new(key, AES.MODE_CTR)
ct_bytes = cipher.encrypt(data)
nonce=b64encode(cipher.nonce).decode('utf8') 
ct=b64encode(ct_bytes).decode('utf8')
result = json.dumps({'nonce': nonce, 'ciphertext': ct})
print('암호문: ', result)

# 수신자가 복호화 
try: 
    b64 = json.loads(result)
    nonce=b64decode(b64['nonce'])
    ct=b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    pt = cipher.decrypt(ct).decode('utf8')
    print('복호화 평문: ', pt)
except ValueError as KeyError:
    print('복호화 에러...') 
