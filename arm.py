num = int(raw_input())
sum = 0
num = n
while n > 0:
   digit = n % 10
   sum += digit ** 3
   n //= 10
if num == sum:
   print ("yes")
else:
   print ("no")
