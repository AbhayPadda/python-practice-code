leftShore       = ['Cabbage','Goat','Wolf']
rightShore      = []
solution        = []

def isSafeShore(objectToMove, shore):
	unsafeCombination1 = ['Cabbage', 'Goat']
	unsafeCombination2 = ['Goat', 'Wolf']
	remaining = shore.copy()
	if (objectToMove):
		remaining.remove(objectToMove)

	remaining.sort()

	if (remaining == unsafeCombination1 or remaining == unsafeCombination2):
		return False
	else:
		return True

def moveObject(lastDirection, objectMoved):
	if (lastDirection == 'left'):
		leftShore.remove(objectMoved)
		rightShore.append(objectMoved)
		return 'right'
	else:
		rightShore.remove(objectMoved)
		leftShore.append(objectMoved)
		return 'left'

def changeDirection(direction):
	if (direction == 'left'):
		return 'right'
	else:
		return 'left'

def findSol():
	movableObjects     = []
	lastMovedDirection = 'left'
	lastObjectMoved    = ''
	step               = ''

	while (len(rightShore) != 3):
		if lastMovedDirection == 'left':
			movableObjects = leftShore
		else:
			movableObjects = rightShore

		step = 'Man'

		if ((len(movableObjects) == 1 and lastMovedDirection == 'right') or (len(movableObjects) !=3 and isSafeShore('', movableObjects) and lastMovedDirection == 'right')):
				lastMovedDirection    = changeDirection(lastMovedDirection)
				lastObjectMoved       = '' 
		else:
			
			for movableObject in movableObjects:
				if (isSafeShore(movableObject, movableObjects) and lastObjectMoved != movableObject):
					lastMovedDirection    = moveObject(lastMovedDirection, movableObject)
					lastObjectMoved = movableObject
					step += ' and ' + lastObjectMoved
					break
		step += ' rowed to ' + lastMovedDirection + ' shore'
		solution.append(step)

print ("\n\n" + format('Man-Cabbage-Wolf-Goat Problem', "^60"))
print ('Group Members: Abhay Padda(193), Deepak(203), Dhananjai(205), Jibson(209)')
print (format('-', '-<80'))
print ("\nInitial Status: ")
print ('Right Shore:- ')
print (rightShore)
print ('Left Shore:- ')
print (leftShore)
print ("\n\n" + format('Finding Solution:', '>30'))

findSol()
			
if (len(rightShore) == 3):
	print ('Successfully moved all three to right shore')
	count = 1
	for step in solution:
		print ("Step %d: %s" %((count), step))
		count += 1