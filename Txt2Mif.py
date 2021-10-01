def convert(filename,outputname):
    fileR = open(filename, "r")
    fileW = open(outputname, "w")
    depth=0
    address = 0
    rAdd=0
    for line in fileR:
        depth+=1
    depth*=8
    fileW.write('DEPTH = ' + str(depth) + '; \n WIDTH = 8; \n ADDRESS_RADIX = UNS; \n DATA_RADIX = HEX; \n CONTENT \n BEGIN \n')
    fileR.close()
    fileR = open(filename, "r")
    for newline in fileR:
        newword=newline
        rAdd=address*8
        for i in newword:
            strA=str(rAdd)
            strR=(str(hex(ord(i))).split('0x')[1]).ljust(2,'0')
            fileW.write(strA + ':' + strR + '; \n')
            rAdd+=1
        address+=1
    fileW.write('END;')
    fileW.close()
    fileR.close()

filename = input()
outputname=input()
convert(filename,outputname)
