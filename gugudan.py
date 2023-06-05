print('곱셈테이블 출력')
for x in range(0, 10): 
    print(f'------', end='\t')
print()
print(f'| X', end='\t')
for x in range(1, 10): 
    print(f'| {x}', end='\t')
for x in range(0, 10): 
    print(f'------', end='\t')
print()

for x in range(1, 10):
    print(f'| {x}', end='\t')
    for y in range(1, 10): 
        print(f'| {x*y}', end='\t')
    print()
