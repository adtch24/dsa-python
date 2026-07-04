# Example used to demonstrate O(log n) time complexity
def find_name(names,target):
    left=0
    right=len(names)-1
    while(left<=right):
        middle=(left+right)//2
        if(names[middle]==target):
           return middle
        elif(names[middle]<=target):
           left = middle+1
        else:
            right=middle-1
    return -1
names=["Aditya","Bunny","Cat","David","Enna"]   # Should be in alphabetical order
target="Enna"
result=find_name(names,target)
if(result==-1):
 print("Not found")
else:
   print("Found at index",result)