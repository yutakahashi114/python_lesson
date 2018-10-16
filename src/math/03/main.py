from collections import Counter

shortlist = [1, 2, 3]
print(sum(shortlist))

samplelist = [4, 1, 3]
samplelist.sort()
print(samplelist)

simplelist = [4, 2, 1, 3, 4]
c = Counter(simplelist)
print(c.most_common())
print(c.most_common(1)[0])
print(c.most_common(3)[1][0])
