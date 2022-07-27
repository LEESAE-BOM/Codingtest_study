document = input()
find = input()

cnt = 0
index = 0

for i in range(len(document)):
    
    if index > i:
        continue
    
    if find == document[i:i+len(find)]:
        cnt+=1
        index = i + len(find)
    else:
        index += 1
        
print(cnt)