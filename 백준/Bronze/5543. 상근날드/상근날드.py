a = 2000
b = 2000
    
for i in range(3):
    a = min(a, int(input()))
for i in range(2):
    b = min(b, int(input()))
    
print(a+b-50)