#mass divided by 3, rounded down, subtract 2, sum
num_list = [#numbers in the list]
#create empty list to hold results
fuel_list = []
#divide by 3 using floor function (round down) and subtract 2
for i in num_list:
    fuel_list.append(i//3 -2)
#sum the new list and print it
print(sum(fuel_list))
