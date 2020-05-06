#My Method
x=int(input())
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(any([True if i==x else False for i in d.keys()]))

#Given Solution
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)
