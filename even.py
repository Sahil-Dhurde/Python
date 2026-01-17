no=5432
sum=0
rev=0
while no>0:
      digit =no%10
      print(digit)
      if digit%2==0:
            print("even number",digit)
            sum=sum *10 + digit
      else:
            print("odd number",digit)
      no=no//10
print("sum of even digits",sum)
ab=sum
while sum>0:
      digit=sum%10
      print(digit)
      rev=rev*10+digit
      sum=sum//10
print("reverse of sum of even digits",rev)
