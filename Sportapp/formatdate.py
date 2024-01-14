from datetime import date


def definepair(chiffre):
    
    if (chiffre %2)== 0:
        
        return True
    else:
        return False
        
print(len(str()))
def fordate(day,month):
    
    today=date.today()
    months=today.month+12
    years=today.year
    days=today.day+12
    if definepair(months)==False:
        frmt={}
        dateboucle=[{'day':days},{'months':months}]
        
        if len(str(days))==1 or len(str(months))==1 :
            if len(str(days))==1:
               frmt['dayformat']='0'+str(days)
            else:
               frmt['dayformat']=str(days)    
            if   len(str(months))==1 :
               frmt['monthformat']= '0'+str(months)
            else:
               frmt['monthsformat']=str(months)     
            return frmt
        else:
            frmt['dayformat']=str(days)
            frmt['monthformat']=str(months)
    else:
        return'rf'
            
    
print(fordate(1,1))