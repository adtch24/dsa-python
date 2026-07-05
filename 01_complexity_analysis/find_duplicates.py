# Example used to demonstrate O(n^2) time complexity
def find_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!= j and numbers[i]==numbers[j]:
                return True
    return False
numbers=[1,25,4,6,9,74,5]
result=find_duplicates(numbers)
if result:
    print("duplicate found")
else:
    print("N0o duplicate found")