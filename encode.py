from base64 import b64encode, b64decode 

p = "Hello 한글"

# string <--> byte 
print('String: ', p)
utf8 = p.encode('utf-8')
print('byte: ', utf8)    # 암호함수 사용시 
p1 = utf8.decode('utf8') 
print('String: ', p1)

# byte <--> base64 
print('Byte: ', utf8)
b64 = b64encode(utf8)
print('Base64: ', b64)   # 전송, 파일저장
b64d = b64decode(b64) 
print('Byte: ', b64d) 

# string <--> base64
print('String: ', p)
b = b64encode(p.encode('utf8'))
print('Base64: ', b)
p1 = b64decode(b).decode('utf8')
print('String: ', p1)
