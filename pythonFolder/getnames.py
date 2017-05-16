logic = [[],[],[],[],[],[]]

def getTag(index,ftype):
    if(ftype == 'jk'):
        tag = (index%2 > 0) 'k' : 'j'
        tagindex = int(len(logic)/2) - int(index/2) - 1
    elif(ftype == 'd'):
        tag = 'd'
        tagindex = 0
    return (tag + str(tagindex))
    

for i in range(len(logic)):
    if(i%2 > 0):
        tag = 'k'
    else:
        tag = 'j'
    tagindex = int(len(logic)/2) - int(i/2) - 1

    print(tag + str(tagindex))