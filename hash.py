from Crypto.Hash import MD5, SHA1, SHA256, SHA224, SHA512, SHA384, SHA3_256, SHAKE256 

message1 = "Hash Test 1..한글테스트..迫った妊婦たちにかつてない意见反馈 · 帮助中心." 
msg1 = message1.encode('utf-8')

h = MD5.new()
h.update(msg1)
print("MD5: "+h.hexdigest())

h = SHA1.new()
h.update(msg1)
print("SHA1: "+h.hexdigest())

h = SHA224.new()
h.update(msg1)
print("SHA224: "+h.hexdigest())

h = SHA256.new()
h.update(msg1)
print("SHA256: "+h.hexdigest())

h = SHA384.new()
h.update(msg1)
print("SHA384: "+h.hexdigest())

h = SHA512.new()
h.update(msg1)
print("SHA512: "+h.hexdigest())

h = SHA3_256.new()
h.update(msg1)
print("SHA3_256: "+h.hexdigest())


