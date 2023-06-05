import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes 

# 송신자가 암호화 
data = "secret 한글 포함 문서".encode('utf8')
key = get_random_bytes(16)  # 128: 16, 192: 24, 256: 32
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data, AES.block_size))
iv=b64encode(cipher.iv).decode('utf8') 
ct=b64encode(ct_bytes).decode('utf8')
result = json.dumps({'iv': iv, 'ciphertext': ct})
print('암호문: ', result)

# 수신자가 복호화 
try: 
    b64 = json.loads(result)
    iv=b64decode(b64['iv'])
    ct=b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf8')
    print('복호화 평문: ', pt)
except ValueError as KeyError:
    print('복호화 에러...') 
