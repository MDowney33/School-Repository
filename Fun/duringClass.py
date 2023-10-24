
num2=3
num1=2

def adding(a, b):
    c = a+b
    d = a-b
    return [c, d]

j = adding(num2, num1)
k = j[0]
l = j[1]

for i in j:
     print(i)

print(j)
print(k)
print(l)
