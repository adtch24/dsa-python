# Fast way to find duplicates
def find_duplicates_fast(numbers):
  look=set()
  for number in numbers:
    if number in look :
      return True
    look.add(number)
  return False
numbers=[12,34,56,78,12]
result=find_duplicates_fast(numbers)
if result:
  print("Duplicates found")
else:
  print("Duplicates not found")
      
