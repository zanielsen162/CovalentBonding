elemSym = ['H', 'B', 'C', 'N', 'O', 'F', 'Si', 'P', 'S', 'Cl', 'Se', 'Br', 'I']
elemCharge = [1, 3, 4, 5, 6, 7, 4, 5, 6, 7, 6, 7, 7]
elemNeeded = [2, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]

axeForms = ['AX1', 'AX2', 'AX1E', 'AX3', 'AX2E', 'AX1E2', 'AX4', 'AX3E', 'AX2E2', 'AX1E3']
moleGeo = ['Linear', 'Linear', 'Linear', 'Trigonal Planar', 'Bent', 'Linear', 'Tetrahedral', 'Trigonal Pyramid', 'Bent', 'Linear']

print(elemSym)

centerSym = input("Center Atom: ")
if centerSym not in elemSym or centerSym == "H":
  while centerSym not in elemSym or centerSym == "H":
    centerSym = input("Please Select a Different Atom: ")

edgeSym = input("Edge Atom: ")
if edgeSym not in elemSym:
  while edgeSym not in elemSym:
    edgeSym = input("Please Select a Different Atom: ")

def testing(numEdge, out):
  global numDouble
  global numTriple
  global centerLonePairs
  global edgeLonePairs
  global electCountCenter
  global totalEAdjust
   
  totalE = numEdge * elemCharge[elemSym.index(edgeSym)] + elemCharge[elemSym.index(centerSym)]
  totalEAdjust = totalE
  
  electCountEdge = []
  electCountCenter = 0
  
  #single bond
  for i in range(0, numEdge):
    #saying it has two even though there is the overlap, but so can compare to see if octet
    electCountEdge.append(2)
    electCountCenter += 2
    #still only subtract two since really only two are used to give appearance since sharing e-
    totalEAdjust -= 2
  
  #make remainder edge lone pairs
  edgeLonePairs = []
  centerLonePairs = 0
  for i in range(0, numEdge):
    edgeLonePairs.append(0)
  
  if edgeSym != 'H':
    if totalEAdjust > 0:
      index = 0
      while totalEAdjust >= 0 and electCountEdge[index] < 8 and totalEAdjust - 2 != 1:
        electCountEdge[index] += 2
        edgeLonePairs[index] += 1
        totalEAdjust -= 2
        if (index + 1) >= len(electCountEdge):
          index = 0
        else:
          index += 1
  else:
    while totalEAdjust > 0 and totalEAdjust - 2 != 1 and electCountCenter < elemNeeded[elemSym.index(centerSym)]:
      electCountCenter += 2
      totalEAdjust -= 2
      centerLonePairs += 1

  #if more left, add them to the center atom
  if totalEAdjust > 0:
    while totalEAdjust > 0 and totalEAdjust - 2 != 1 and electCountCenter < elemNeeded[elemSym.index(centerSym)]:
      electCountCenter += 2
      totalEAdjust -=2
      centerLonePairs += 1
  
  #if center doesn't have octet, double bonds!
  numDouble = 0
  numTriple = 0
  if edgeSym != "H":
    while electCountCenter < elemNeeded[elemSym.index(centerSym)] and numDouble < numEdge:
      electCountCenter += 2
      edgeLonePairs[numDouble] -= 1
      numDouble += 1
    
    #if center doesn't have octet, triple bonds
    while electCountCenter < elemNeeded[elemSym.index(centerSym)] and numTriple < numEdge:
      electCountCenter += 2
      numDouble -= 1
      edgeLonePairs[numTriple] -= 1
      numTriple += 1
  
  if out != True:
    return totalEAdjust
  elif out == True:
    return electCountCenter


def axeFormula(x, e, out):
  if e > 1:
    formula = "AX" + str(x) + "E" + str(e)
  elif e > 0:
    formula = "AX" + str(x) + "E"
  else:
    formula = "AX" + str(x)

  if out == True:
    return formula
  else:
    return moleGeo[axeForms.index(formula)]


def makeModel(numEdge, edgeSym, centerSym, numDouble, numTriple):

  edge = []
  bond = []

  for i in range(0, numEdge):
    edge.append(edgeSym)
  for h in range(0, numDouble):
    if len(bond) > 2:
      bond.append("║")
    else:
      bond.append("═")
  for j in range(0, numTriple):
    if len(bond) > 2:
      bond.append("│║")
    else:
      bond.append("☰")
  
  while len(bond) < numEdge:
    if len(bond) >= 2:
      bond.append("│")
    else:
      bond.append("─")
  
  listAtoms = []

  if numEdge > 0:
    atom1 = edge[0], " ", bond[0], " ", centerSym
    listAtoms.append("".join((str(a)for a in atom1)))
  if numEdge > 1:
    atom2 =  " ", bond[1], " ", edge[1]
    listAtoms.append("".join((str(a)for a in atom2)))
  if numEdge > 2:
    atom3 = "    ", edge[2], "\n", "    ", bond[2], "\n"
    listAtoms.insert(0, "".join((str(a)for a in atom3)))
  if numEdge > 3:
    atom4 = "\n", "    ", bond[3], "\n", "    ", edge[3]
    listAtoms.append("".join((str(a)for a in atom4)))
    
  return("".join((str(a)for a in listAtoms)))

numEdgeOps = []
for i in range(1, 5):
  if testing(i, False) == 0 and testing(i, True) == elemNeeded[elemSym.index(centerSym)]:
    numEdgeOps.append(i)

while len(numEdgeOps) == 0:
  edgeSym = input("Please Select a Different Atom: ")
  for i in range(1, 5):
    if testing(i, False) == 0 and testing(i, True) == elemNeeded[elemSym.index(centerSym)]:
      numEdgeOps.append(i)
print("Amount of Edge Options: " + str(numEdgeOps))

numEdge = int(input("Amount of Edge: "))
while numEdge not in numEdgeOps:
  numEdge = int(input("Please Select from Above: "))

testing(numEdge, "x")
print("\n")
print(makeModel(numEdge, edgeSym, centerSym, numDouble, numTriple))
print("\n")
print("Edge Lone Pairs: " + str(edgeLonePairs))
print("Center Lone Pairs: " + str(centerLonePairs))
print("Molecular Geometry: " + axeFormula(numEdge, centerLonePairs, False))
