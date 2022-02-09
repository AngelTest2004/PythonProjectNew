import  pickle
a=[1,2,3,4,5]


re=pickle.dumps(a)


with open ('C:\\temp\\1.txt','wb') as f:
    f.write(pickle.dumps(a))
    pickle.dump(a,f)

with open ('C:\\temp\\1.txt','rb') as f:
   #re=f.read()
   re_2=pickle.load(f)

#print(pickle.loads(re))
print(re_2)


