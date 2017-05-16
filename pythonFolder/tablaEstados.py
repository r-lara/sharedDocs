import sys
import time

# user input
states = int( input('States (count from 0): ') )
inVars = int( input('Inputs: ') )     # A B (buttones o senales digitales)
outVars = int( input('Outputs: ') )    # controla las salidas

# calculated
bitsState = len(format(states,'b'))
bitsIn = inVars
bitsOut = outVars


"""
Estructura de datos
    [
        [in,state,next,out],
        [11,101,110,10]
    ]
"""


""" Init Functions """
def printTable(arr):
    print ()
    print ("In Actu  Next  Out FlipFlops")
    for dato in arr:
        print (dato)
    print()
    return

def confirm(msg):
    print(msg)
    conf = False
    while (not conf):
        ui = input("Confimr [y/n]: ").lower
        if(ui == 'y'):
            conf = True
    return

def getFlipFlop():
    print()
    flipflop = input('Select FlipFlop Type [jk,d]: ')
    if(flipflop == 'jk' or flipflop == 'd'):
        return flipflop
    else:
        getFlipFlop()

def getFlipTable(flpType,actualBit,nextBit):
    if(flpType == 'jk'):
        conv = actualBit + nextBit
        if conv == '00':
            return '0x'
        elif conv == '01':
            return '1x'
        elif conv == '10':
            return 'x1'
        elif conv == '11':
            return 'x0'
        else:
            return 'xx'
    elif(flpType == 'd'):
        if nextBit == '1':
            return '1'
        elif nextBit == '0':
            return '0'
        else:
            return 'xx'

logic = []
def getMaps(arr):
  length = len(arr)
  numeroTablas = (len(arr[0]) - 4)*2
  """
  logic = [
    [0,1,x ..], # j2
    [0,1,x ..], # k2
    [0,1,x ..], # j1
    [0,1,x ..]  # k1
  ]
  """

  for i in range(numeroTablas):
    logic.append([])

  for i in range(length):
    dato = datos[i]  # ['0', '00', '11', '1', '1x', '1x']
    for x in range(int(numeroTablas/2)):
      bit = list(dato[x+4])
      logic[(x*1) + x].append(bit[0])
      logic[(x*1) + 1 + x].append(bit[1])


  #print(logic)
  return


""" End Functions """

# Genera Tabla de Verdad con BitsEstados y InputVariales
datos = []
for x in range(0,2**inVars):
    bi1 = format(x,'b').zfill(bitsIn)
    for y in range(0,2**bitsState):
        bi2 = format(y,'b').zfill(bitsState)
        datos.append( [ bi1 , bi2 ] )
        #print (bi1 + " " + bi2)
#print ("datos len ",len(datos))

# # Get state description
descrState = []
for i in range(0,states+1):
    descrState.append(input('s%i: ' % i))
#print (descrState)

## confirm('')
print()
print("extState.outVals => 3.101 <= [dec.bin]")
print()
for x in range(0,2**bitsState):
    # por cada estado
    for y in range(0, 2**inVars):
        # asignar estado siguiente
        #print( "%s : %s" % (x,y))
        nextStateInput = False
        while (not nextStateInput):
            userIn = input('s%i & in %s : s ' % (x,format(y,'b').zfill(inVars)))
            i = userIn.find(".")
            if( (len(userIn) >= 3 ) and (i >= 0) ):
                userData = userIn.split('.')
                index = (2**bitsState)*y + x
                if(userData[0] == 'x'):
                    datos[index].append(''.zfill(bitsState).replace('0','x'))
                    nextStateInput = True
                else:
                    userData[0] = format(int(userData[0]),'b').zfill(bitsState)
                    datos[index].append(userData[0])
                    nextStateInput = True
                if(userData[1] == 'x'):
                    datos[index].append(''.zfill(bitsIn).replace('0','x'))
                    nextStateInput = True
                else:
                    datos[index].append(userData[1])
                    nextStateInput = True

                printTable(datos)


print ("total combinations: %s" % 2 ** ( states + inVars ))

# Get FlipFlop type
flipType = getFlipFlop()
# Creates Truth Table
for dato in datos: # [10,100,110,1] => [inputs,actualState,nextState,outputs]
    actuBits = list(dato[1]) # 100 => [1,0,0]
    nextBits = list(dato[2]) # 110 => [1,1,0]
    for bit in range(len(actuBits)):
        dato.append(getFlipTable(flipType,actuBits[bit],nextBits[bit]))

printTable(datos)
getMaps(datos)

for i in range(len(logic)):
	if(len(logic[0]) == 16):
		if(i%2 > 0):
			print("k%i" % (len(datos[0]) / 2 - i/2))
		else:
			print("j%i" % (len(datos[0]) / 2 - i/2))
		print ( "" )
		print (" %s | %s | %s | %s" % ( logic[i][0].replace('0',' '),  logic[i][1].replace('0',' '),  logic[i][3].replace('0',' '),  logic[i][2].replace('0',' ') ))
		print ("---+---+---+---")
		print (" %s | %s | %s | %s" % ( logic[i][4].replace('0',' '),  logic[i][5].replace('0',' '),  logic[i][7].replace('0',' '),  logic[i][6].replace('0',' ') ))
		print ("---+---+---+---")
		print (" %s | %s | %s | %s" % ( logic[i][12].replace('0',' '), logic[i][13].replace('0',' '), logic[i][15].replace('0',' '), logic[i][14].replace('0',' ') ))
		print ("---+---+---+---")
		print (" %s | %s | %s | %s" % ( logic[i][8].replace('0',' '),  logic[i][9].replace('0',' '),  logic[i][11].replace('0',' '), logic[i][10].replace('0',' ') ))
		print
		print

	elif(len(logic[0]) == 32):
		if(i%2 > 0):
			print("k%i" % (len(datos[0]) / 2 - i/2))
		else:
			print("j%i" % (len(datos[0]) / 2 - i/2))
		print ( "" )
		print (" %s | %s | %s | %s" % ( logic[i][0].replace('0',' '),      logic[i][1].replace('0',' '),      logic[i][3].replace('0',' '),      logic[i][2].replace('0',' ') ))
		print ("---+---+---+---")
		print (" %s | %s | %s | %s" % ( logic[i][4].replace('0',' '),      logic[i][5].replace('0',' '),      logic[i][7].replace('0',' '),      logic[i][6].replace('0',' ') ))
		print ("---+---+---+---")
		print (" %s | %s | %s | %s" % ( logic[i][12].replace('0',' '),     logic[i][13].replace('0',' '),     logic[i][15].replace('0',' '),     logic[i][14].replace('0',' ') ))
		print ("---+---+---+---")
		print (" %s | %s | %s | %s" % ( logic[i][8].replace('0',' '),      logic[i][9].replace('0',' '),      logic[i][11].replace('0',' '),     logic[i][10].replace('0',' ') ))
		print
		print (" %s | %s | %s | %s" % ( logic[i][0+16].replace('0',' '),   logic[i][1+16].replace('0',' '),   logic[i][3+16].replace('0',' '),   logic[i][2+16].replace('0',' ') ))
		print ("---+---+---+---")
		print (" %s | %s | %s | %s" % ( logic[i][4+16].replace('0',' '),   logic[i][5+16].replace('0',' '),   logic[i][7+16].replace('0',' '),   logic[i][6+16].replace('0',' ') ))
		print ("---+---+---+---")
		print (" %s | %s | %s | %s" % ( logic[i][12+16].replace('0',' '),  logic[i][13+16].replace('0',' '),  logic[i][15+16].replace('0',' '),  logic[i][14+16].replace('0',' ') ))
		print ("---+---+---+---")
		print (" %s | %s | %s | %s" % ( logic[i][8+16].replace('0',' '),   logic[i][9+16].replace('0',' '),   logic[i][11+16].replace('0',' '),  logic[i][10+16].replace('0',' ') ))
		print
		print

	elif(len(logic[0]) == 8):
		if(i%2 > 0):
			print("k%i" % (len(logic) / 2 - i/2 - 1))
			print("k%i" % (len(logic) / 2 - i/2 - 1))
		else:
			print("j%i" % (len(logic[0]) / 2 - i/2 - 1))
		print (" %s | %s | %s | %s" % ( logic[i][0].replace('0',' '),  logic[i][1].replace('0',' '),  logic[i][3].replace('0',' '),  logic[i][2].replace('0',' ') ))
		print ("---+---+---+---")
		print (" %s | %s | %s | %s" % ( logic[i][4].replace('0',' '),  logic[i][5].replace('0',' '),  logic[i][7].replace('0',' '),  logic[i][6].replace('0',' ') ))
		print()
		print()

	elif(len(logic[0]) == 4):
		if(i%2 > 0):
		    print("k%i" % (len(datos[0]) / 2 - i/2 - 1))
		else:
			print("j%i" % (len(datos[0]) / 2 - i/2 - 1))
		print ( "" )
		print (" %s | %s " % ( logic[i][0].replace('0',' '),  logic[i][1].replace('0',' ') ))
		print ("---+---")
		print (" %s | %s " % ( logic[i][2].replace('0',' '),  logic[i][3].replace('0',' ') ))
		print()
		print()


