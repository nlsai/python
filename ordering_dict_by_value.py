#My Method
d = {'Math':911, 'Physics':13833, 'Chemistry':8788}
x=d.keys()
y=d.values()
z=dict(zip(y,x))
print({v:k for k,v in sorted(z.items()) })
print({v:k for k,v in sorted(z.items(),reverse=True) })

#Given Method
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1)))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
