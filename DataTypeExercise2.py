Cars = [56,78,34,21,56,34,125,45,89,75,12,56,]
print(Cars)
print("Smallest Number:",min(Cars))
print("Largest Number:",max(Cars))
Sum = sum(Cars)
print("Sum of the numbers:",Sum)
res = list(dict.fromkeys(Cars))
print ("No Duplicates:",str(res))