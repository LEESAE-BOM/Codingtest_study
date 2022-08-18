a= input()
ho = int(a[0:2])
mo = int(a[3:5])
so = int(a[6:8])
b= int(input())
c= int(input())
b=b*(c-1)
h = int(b/3600)
m = int((b%3600)/60)
s = int(b%60)
sf=(so+s)%60
if so+s>=60:
    mo+=1
mf=(mo+m)%60
if mo+m>=60:
    ho+=1
hf=(ho+h)%24
print(str(hf).zfill(2)+':'+str(mf).zfill(2)+':'+str(sf).zfill(2))
