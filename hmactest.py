from Crypto.Hash import HMAC, SHA256, SHA512

# 송신자 
secret = b'kjgfljslkjfgkfljsdf'
message = b'Helloworld'
h = HMAC.new(secret, digestmod=SHA512)
h.update(message)
hmac = h.hexdigest()
print('송신자 메시지 인증코드: ', hmac)
# 송신자->수신자 <message, hmac>

# 수신자 
secret1 = b'kjgfljslkjfgkfljsdf'
message1 = message
h1 = HMAC.new(secret1, digestmod=SHA512)
h1.update(message1)
hmac1 = hmac
try:
    h1.hexverify(hmac1)
    print("The message '%s' is authentic" % message1)
except ValueError:
    print("The message or the key is wrong")
