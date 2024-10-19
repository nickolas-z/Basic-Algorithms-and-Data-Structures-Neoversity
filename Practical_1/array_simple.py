import array as arr
import sys

a = arr.array('i', [1, 2, 3])

print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")

b = arr.array('d', [2.5, 3.2, 3.3])
print("\n",type(b), sys.getsizeof(b[:]))

print("\nThe new created array is : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
print()

c = [2.5, 3.2, 3.3]
print(type(c), sys.getsizeof(c.copy))

print(id(b[0]))
print(id(b[1]))

print(id(c[0]))
print(id(c[1]))