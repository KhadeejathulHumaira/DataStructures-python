#Insertion Sort
def sortArr(arr):
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[i]>arr[j]:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
  return arr


arr = [1000, 11, 445, 1, 330, 3000]
k=3
print(sortArr(arr)[k-1])

# Much optimized one
new_arr=sorted(arr)
value= new_arr[k-1]
print(value

