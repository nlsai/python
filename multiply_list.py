#My Method
v,c=[1,2,3,4,5],1
for i in v:
  c*=i
print(c)

#Given Solution
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,-8]))
