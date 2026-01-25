a='apple'
for i in range(len(a)):
         if a[i] not in a[:i]:
            print(a[i],end='')