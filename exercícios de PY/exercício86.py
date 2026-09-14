Temp = []
Princ = []
Mai = Men = 0
while True:
    Temp.append (str (input( 'no me ')))
    Temp.append (float (input ('peso')))
    if len (Princ) ==0:
        Mai = Men = Temp[1]
    else:
        if Temp[1] > Mai:
          Mai = Temp[1]
        if Temp[1]< Men:
            Men = Temp[1]
        Princ.append (Temp [:])
        Temp.clear()