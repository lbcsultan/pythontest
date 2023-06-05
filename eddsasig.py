from Crypto.PublicKey import ECC # 키생성, 암호시스템 
from Crypto.Signature import eddsa # 전자서명 알고리즘 
from Crypto.Hash import SHA512 
from base64 import b64encode, b64decode 

#1. 타원곡선암호(ECC) 키생성 
key = ECC.generate(curve='ed25519') # p192, p224, p256, p384, p521, ed25519, ed448 
privateKey = key 
publicKey = key.public_key()
privateKeyPem = privateKey.export_key(format='PEM')
publicKeyPem = publicKey.export_key(format='PEM')
print('개인키: ', privateKeyPem)
print('공개키: ', publicKeyPem)

#2. 파일에 저장하기, 읽어오기 
f = open('myprivatekey.pem', 'wt')
f.write(privateKeyPem)
f.close()

f = open('mypublickey.pem', 'wt')
f.write(publicKeyPem)
f.close()

f = open('myprivatekey.pem', 'rt')
privateKey1 = ECC.import_key(f.read())
f.close()

f = open('mypublickey.pem', 'rt')
publicKey1 = ECC.import_key(f.read())
f.close()

# 서명할 메시지 
message = 'To be signed. 한글메시지.【速報】大阪府で過去最多1260人の感染確認. 央视评副处长体验送外卖累瘫街头.'
messageUtf8 = message.encode("utf-8")

#3. 송신자(서명자)의 서명 생성: 서명자의 개인키 사용 
h = SHA512.new(messageUtf8)
signer = eddsa.new(privateKey, 'rfc8032') 
signature = signer.sign(h) 
sig_b64 = b64encode(signature).decode('utf8') 
print('EDDSA 서명: ', sig_b64)
# 송신자가 수신자에게 <message, signature>를 전송 

#4. 수신자(검증자)의 서명 검증: 서명자의 공개키 사용 
message = 'To be signed. 한글메시지.【速報】大阪府で過去最多1260人の感染確認. 央视评副处长体验送外卖累瘫街头.'
messageUtf8 = message.encode("utf-8")
h = SHA512.new(messageUtf8)
verifier = eddsa.new(publicKey1, 'rfc8032')
try: 
    verifier.verify(h, signature)
    print('서명 검증 성공')
except ValueError:
    print('서명이 유효하지 않습니다...')
