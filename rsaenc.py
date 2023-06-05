from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

#1. RSA 키쌍 생성 
key = RSA.generate(2048) 

#2. 개인키를 파일로 저장 
private_key = key.export_key() 
file_out = open("privateKey.pem", 'wb')
file_out.write(private_key)
file_out.close()
print("RSA 개인키: \n", private_key)

#3. 공개키를 추출하고 파일에 저장 
public_key = key.publickey().export_key()
file_out = open('publicKey.pem', 'wb')
file_out.write(public_key)
file_out.close()
print("RSA 공개키: \n", public_key)

#4. 공개키를 개인키로부터 추출 
key1 = RSA.import_key(private_key)
public_key_1 = key1.publickey().export_key()
print("RSA 공개키1: \n", public_key_1)

#5. 개인키의 패스워드 암호화 파일 저장 
password = 'dslkjslkjfdlkjfhdfkjhkdf'
encrypted_key = key.export_key(passphrase = password, pkcs = 8, protection = 'scryptAndAES128-CBC')
file_out = open('privateKeyEncrypted.pem', 'wb')
file_out.write(encrypted_key)
file_out.close()

#6. 패스워드 암호화 저장된 RSA 개인키를 읽어옴 
password1 = password
encoded_key = open('privateKeyEncrypted.pem', 'rb').read()
key2 = RSA.import_key(encoded_key, passphrase=password1)
print("RSA 개인키2: \n", key2.export_key())
print("RSA 공개키2: \n", key2.publickey().export_key())

#7. RSA 암호화 (송신자)
# 송신자가 수신자의 공개키로 암호화하여 전송 
plaintext =  'Hello world. 헬로월드. 반갑습니다'.encode('utf-8')
file_out = open('encrypted_data.bin', 'wb')

recipient_key = RSA.import_key(open('publicKey.pem').read()) 
session_key = get_random_bytes(16) # AES 암호화를 위한 난수키 

# 세션키를 수신자의 공개키로 암호화  
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# AES로 데이터 암호화 
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(plaintext)
[file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
file_out.close()
# 송신자는 수신자에게 encrypted_data.bin 파일을 전송합니다. 

#8. 수신자의 복호화 
file_in = open('encrypted_data.bin', 'rb') 
private_key = RSA.import_key(open('privateKey.pem').read())

enc_session_key, nonce, tag, ciphertext = [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

# 세션키 복구 
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

# AES 대칭키 복호화 
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
recoveredtext = cipher_aes.decrypt_and_verify(ciphertext, tag)
print("복호화 텍스트: ", recoveredtext.decode('utf-8'))