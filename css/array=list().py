array=list()
num = input("Enter Input" )
print ("Integer Input " )
for i in range(int(num)):
    n = int(input('input :'))
    array.append(int(n))
print(array)
c=0
a=1
b=1
if array==0 or array==1:
    print("1")
else:
    while c<array:
        c=a+b
        b=a
        a=c
        if c==array:
            print("1")
        else:
            print("0")