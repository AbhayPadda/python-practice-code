solution = []

def findSol(diskCount, source, destination, helper):
    if diskCount >= 1:
        findSol(diskCount - 1, source, helper, destination)
        solution.append('From ' + source + ' to ' + destination)
        findSol(diskCount - 1, helper, destination, source)

findSol(3, "Source", "Destination", "Helper")

print (format('Solution is: ', '^60'))
print (format('', '-<60'))
count = 1

for step in solution:
    print ('Step: %d: %s' %(count, step))
    count += 1
