num = int(raw_input())
if num > 1:
      for i in range(2,num):
	if (num % i) != 0:
		print("yes")
		#print(i,"times",num//i,"is",num)
		break
	else:
		print("no")
       
else:
   print("no")
