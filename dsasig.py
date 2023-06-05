from Crypto.PublicKey import DSA  # 키생성 알고리즘  
from Crypto.Signature import DSS  # 전자서명 알고리즘
from Crypto.Hash import SHA256 
from base64 import b64encode, b64decode

#1. DSA 키생성 
key = DSA.generate(2055)
privateKey = key             # 개인키 
publicKey = key.publickey()  # 공개키 
f = open('public_key.pem', 'wb')
f.write(publicKey.export_key())
f.close() 
print('DSA 개인키: ', privateKey.export_key())
print('DSA 공개키: ', publicKey.export_key())

# 서명할 메시지 
message = 'To be signed. 한글메시지.【速報】大阪府で過去最多1260人の感染確認. 央视评副处长体验送外卖累瘫街头.'
messageUtf8 = message.encode("utf-8")

#2. 송신자(서명자)가 서명 생성: 서명자의 개인키 사용 
h = SHA256.new(messageUtf8)
signer = DSS.new(privateKey, 'fips-186-3')
signature = signer.sign(h)
sig_b64 = b64encode(signature).decode('utf8')
print('DSA 전자서명: ', sig_b64)
# 송신자가 수신자에게 <message, signature>를 전송합니다. 

#3. 수신자(검증자)가 서명 검증: 서명자의 공개키를 사용 
message = 'To be signed. 한글메시지.【速報】大阪府で過去最多1260人の感染確認. 央视评副处长体验送外卖累瘫街头.'
messageUtf8 = message.encode("utf-8")
h = SHA256.new(messageUtf8)
verifier = DSS.new(publicKey, 'fips-186-3')

try: 
    verifier.verify(h, signature)
    print('서명이 유효합니다')
except ValueError:
    print('서명이 유효하지 않습니다. ')