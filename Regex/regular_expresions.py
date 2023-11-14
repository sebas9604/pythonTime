import re
p = re.compile('ab*')
it = p.match("abbqwerabbbbbsdfsfab")
print("Iter:", it, sep = " ")

print(it.span())

d= re.compile('x+')
y = d.sub('-','abxd')
print(y)