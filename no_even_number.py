a=[]
for i in range(0,5):
    i=int(input())
    if i%2==0 :
        print("我討厭偶數")
        break
    else:
        a.append(i)
print(a)