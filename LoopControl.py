for i in range(10):
    print(i)
    if i == 2:
        break

for n in range(10):
    if n == 5:
        continue    
        print(n)

for n in range(10):
    if n == 5:
        pass    
        print(n)  

for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break")

i = 1
while i < 6:
  print(i)
  i+=1
else:
  print("i is no longer less than 6")
 

