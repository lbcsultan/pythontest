import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes 

# 송신자의 파일 암호화 
file_to_encrypt = 'coffee.zip'
input_file = open(file_to_encrypt, 'rb')
output_file = open(file_to_encrypt+'.enc', 'wb')
key = get_random_bytes(32)
buffer_size = 65536 # 64kb

cipher = AES.new(key, AES.MODE_CBC)
output_file.write(cipher.iv)

buffer = input_file.read(buffer_size)
while len(buffer) > 0:
    ciphered_bytes = cipher.encrypt(pad(buffer, AES.block_size))
    output_file.write(ciphered_bytes)
    buffer = input_file.read(buffer_size)
input_file.close() 
output_file.close()

# 수신자가 파일 복호화 
input_file = open(file_to_encrypt+'.enc', 'rb')
output_file = open(file_to_encrypt+'.zip', 'wb')
iv = input_file.read(16)

cipher = AES.new(key, AES.MODE_CBC, iv=iv)

buffer = input_file.read(buffer_size)
while len(buffer) > 0:
    decrypted_bytes = unpad(cipher.decrypt(buffer), AES.block_size)
    output_file.write(decrypted_bytes)
    buffer = input_file.read(buffer_size)

input_file.close()
output_file.close()