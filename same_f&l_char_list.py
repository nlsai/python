#My Method
l=['abc', 'xyz', 'aba', '1221','15555321']
print(len([i for i in l if len(i)>=2 and i[0]==i[-1]]))

#Given Solution
def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))
