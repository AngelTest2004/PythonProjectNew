a=" test asdt,asdf "
print(a)
#去除前后空白字符
print(a.strip())

s="01234567"
print(s[2:4])
print(s[0::2]) #0246
print(s[1::2]) #1357
print(s[::-1]) #从右到左 7654321
print(s[-1:-5:-2]) #从右到左 75

del s
print(s)
