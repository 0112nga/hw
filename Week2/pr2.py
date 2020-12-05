

date=input('Enter a date(mm/dd/yyyy): ')
replace=date.replace('/',' ')
convert=replace.split()
if convert[0]=='01':
        print('January '+convert[1]+', '+convert[2] )
elif convert[0]=='02':
        print('February '+convert[1]+', '+convert[2] )
elif convert[0]=='03':
        print('March '+convert[1]+', '+convert[2] )
elif convert[0]=='04':
        print('April '+convert[1]+', '+convert[2] )
elif convert[0]=='05':
        print('May '+convert[1]+', '+convert[2] )
elif convert[0]=='06':
        print('June '+convert[1]+', '+convert[2] )
elif convert[0]=='07':
        print('July '+convert[1]+', '+convert[2] )
elif convert[0]=='08':
        print('August '+convert[1]+', '+convert[2] )
elif convert[0]=='09':
        print('September '+convert[1]+', '+convert[2] )
elif convert[0]=='10':
        print('October '+convert[1]+', '+convert[2] )
elif convert[0]=='11':
        print('November '+convert[1]+', '+convert[2] )
elif convert[0]=='12':
        print('December '+convert[1]+', '+convert[2] )


