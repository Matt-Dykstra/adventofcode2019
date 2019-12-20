#NOTE - THIS DOESN'T WORK CORRECTLY YET! (so so close...)

inputlist = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,19,6,23,2,13,23,27,1,9,27,31,2,31,9,35,1,6,35,39,2,10,39,43,1,5,43,47,1,5,47,51,2,51,6,55,2,10,55,59,1,59,9,63,2,13,63,67,1,10,67,71,1,71,5,75,1,75,6,79,1,10,79,83,1,5,83,87,1,5,87,91,2,91,6,95,2,6,95,99,2,10,99,103,1,103,5,107,1,2,107,111,1,6,111,0,99,2,14,0,0]

#position 1: 1 = add, 2 = multiply, 99=done
#position 2 and 3: indicate positions of numbers to use for operation
#position 4: position at which result should be stored
#once done, step forward 4 positions
#what value is at position 0 when the program halts?

#before running, replace position 1 with `12` and position 2 with `2`
for i in inputlist:
    inputlist[1] = 12
    inputlist[2] = 2
print(inputlist)    

for i, n in enumerate(inputlist[::4]):
    if n==1:
        print("add")
        #add index values indicated by positions 2 and 3, store result at index value indicated by 4
        x = inputlist[i+1]
        y = inputlist[i+2]
        z = inputlist[i+3]
        print (x,y,z)
        inputlist[z] = inputlist[x] + inputlist[y]
        print(inputlist)
    elif n==2:
        print("multiply")
        #multiply index values indicated by positions 2 and 3, store result at index value indicated by 4
        x= inputlist[i+1]
        y = inputlist[i+2]
        z = inputlist[i+3]
        print (x,y,z)
        inputlist[z] = inputlist[x] * inputlist[y]
        print(inputlist)
    elif n==99:
        break
    else:
        print("woah")
        #this shouldn't happen if I'm doing it right
#print the new list                          
print(inputlist)
#what value is at position 0 when the program halts?
print(inputlist[0])
