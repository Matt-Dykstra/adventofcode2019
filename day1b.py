#requires code in day1a to generate values for fuel_list (which in turn requires input values)
#need to account for fuel needed to move the fuel that moved the existing weight
totalfuel_list = []
for i in fuel_list:
#divide by 3, round down, and subtract 2
#if result is greater than 2, do it again
    while i > 6:
        i=(i//3 -2)
        #add result to a new list
        totalfuel_list.append(i)
        #printing to make sure this makes sense
        print(totalfuel_list)
        #sum the list by itself just to check, then add the sums of the two lists together to get the final value
        print(sum(totalfuel_list))
        print(sum(fuel_list)+(sum(totalfuel_list)))
