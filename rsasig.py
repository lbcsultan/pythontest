from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Signature import pkcs1_15, pss 
from base64 import b64encode, b64decode
from Crypto.Hash import SHA256 

#1. RSA 키쌍 생성 
key = RSA.generate(2048) 
privateKey = key           # 개인키 
publicKey = key.publickey() # 공개키 

# 서명할 메시지 
message = 'To be signed. 한글메시지.【速報】大阪府で過去最多1260人の感染確認. 央视评副处长体验送外卖累瘫街头.'
messageUtf8 = message.encode("utf-8")

#2. RSA 전자서명: PKCS#1 v1.5 
# 송신자(서명자)가 서명 생성 : 서명자의 개인키 
h = SHA256.new(messageUtf8)
signature = pkcs1_15.new(privateKey).sign(h)
sig_b64 = b64encode(signature).decode('utf8')
print('RSA 전자서명(PKCS#1 v1.5): ', sig_b64)
# 송신자가 수신자에게 <message, signature>를 전송 

# 수신자(검증자)가 서명 검증: 서명자의 공개키 
message = 'To be signed. 한글메시지.【速報】大阪府で過去最多1260人の感染確認. 央视评副处长体验送外卖累瘫街头.'
messageUtf8 = message.encode("utf-8")
h = SHA256.new(messageUtf8)
try: 
    pkcs1_15.new(publicKey).verify(h, signature)
    print('서명 검증 성공')
except (ValueError, TypeError): 
    print('서명이 유효하지 않습니다...')

#3. RSA 전자서명: PSS 
# 송신자(서명자)가 서명 생성 : 서명자의 개인키 
h = SHA256.new(messageUtf8)
signature = pss.new(privateKey).sign(h)
sig_b64 = b64encode(signature).decode('utf8')
print('RSA 전자서명(PSS): ', sig_b64)
# 송신자가 수신자에게 <message, signature>를 전송 

# 수신자(검증자)가 서명 검증: 서명자의 공개키 
message = 'To be signed. 한글메시지.【速報】大阪府で過去最多1260人の感染確認. 央视评副处长体验送外卖累瘫街头.'
messageUtf8 = message.encode("utf-8")
h = SHA256.new(messageUtf8)
try: 
    pss.new(publicKey).verify(h, signature)
    print('서명 검증 성공')
except (ValueError, TypeError): 
    print('서명이 유효하지 않습니다...')