x=(10,20,30,40,50)
sum=0
for i in x:
    sum+=i
print(sum)
x=(10,25,37,40,57,65)
sum=0
for i in x:
    if i%10==0:
        print(i)

x=[10,20,30,40,50,30,50]
y=[]
for i in x:
    if i not in y:
        y.append(i)
print(y) 

x=(10,20,30,40,50)
y=(60,70,80,90,100,20)
for i in x:
    if i in y:
        print(i)

