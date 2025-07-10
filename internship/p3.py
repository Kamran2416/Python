str="hii hii hii hii this this thisthis is kamran you are in python world"
ls=str.split()
ans=[]
for l in ls:
    if l in ans:
        pass
    else:
        ans.append(l)
        print(l," is repeated ",ls.count(l)," times")