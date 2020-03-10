# Print List
Cars = [56,78,34,21,56,34,125,45,89,75,12,56,]
print(Cars)
# Print Smallest Number in list
print("Smallest Number:",min(Cars))
# Print Largest Number in list
print("Largest Number:",max(Cars))
# The sum of numbers in the list
Sum = sum(Cars)
print("Sum of the numbers:",Sum)
# Removes the duplicated numbers in the list
res = list(dict.fromkeys(Cars))
print ("No Duplicates:",str(res))