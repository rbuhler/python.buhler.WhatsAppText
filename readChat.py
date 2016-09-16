import os.path

sText = 'text/chat.txt'

# Checks the file exists
if(os.path.isfile(sText)):
	print('File '+sText + ' exists.')

# Reads the file
	nCount = 0
	with open(sText, "r") as sFile:

	    aFile = [] 

	    aDate   = []
	    aTime   = []
	    aPessoa = []
	    aChat   = []

	    for sLine in sFile:
	        aFile.append(sLine)
	        aDate.append(sLine[:8])
	        aTime.append(sLine[9:18])

	        cChar    = ''
	        nPointer = 19
	        sPessoa  = ''
	        while(cChar != ':' ):
	        	cChar    = sLine[nPointer]
	        	sPessoa += cChar
	        	nPointer += 1

	        	print('-> ' + cChar)

	        aPessoa.append(sPessoa)
	        aChat.append(sLine[nPointer:len(sLine)])
	        
		    print(aDate[nCount])
		    print(aTime[nCount])
		    print(aPessoa[nCount])
		    print(aChat[nCount])

		    nCount += 1

	    print('[Numero de linhas] ' + str(len(aFile)))



else:
	print('File '+sText + ' does not exist.')