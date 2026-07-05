# Example used to demonstrate O(n) time complexity
def find_name(names,target):
    for name in names:
        if name==target:
            return True
    
    return False
list=["Arun","Shiv","Adit","Jay"]
target="Adit"
result=find_name(list,target)
if result:
 print("Found")
else:
   print("Not found") 