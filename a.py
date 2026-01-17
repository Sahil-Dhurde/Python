a=121
rev=0
c=a
while a>0:
      digit =a%10
      rev = rev * 10 + digit
      a = a//10
print(rev)
if c == rev:
      print("String is palindrome")
else:
      print("String is not palindrome")