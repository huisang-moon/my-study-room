#1크로아티아 알파벳

word = input()
arr = ["c=","c-","dz=","d-","lj","nj","s=","z="]


for i in arr:
    if i in word :
        word = word.replace(i,"a")
print(len(word))


        
      




