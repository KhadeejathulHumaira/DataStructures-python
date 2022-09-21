# find max and min    
arr = [1000, 11, 445, 1, 330, 3000]
mini=arr[0]
maxi=arr[0]
for i in arr:
  if i<mini:
    mini=i
  if i>maxi:
    maxi=i
print(mini,maxi)
