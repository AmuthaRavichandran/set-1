num1=int(raw_input())
num2=int(raw_input())
for num in range(num1,num2 + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
