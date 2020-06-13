#python 2.7.15

l1=[1,"sai", 2,"siva",3,"ravi",4,"shannu"]
a=l1[::2]
b=l1[1::2]
c={a[i]:b[i] for i in range(len(a))}
print(c)
