from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('D:\\Cursos Python\\newtext.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

try:
    bf = open('D:\\Cursos Python\\newtext.bin', 'rb')
    data = bytearray(bf.read(3))
    
    while len(data)> 0:
        for b in data:
            print(hex(b), end=' ')
        print()
        data = bytearray(bf.read(3))
    bf.close()

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
