
import  string

def has_digits(psw):
    if any(char.isdigit() for char in psw):
        return True
    else :
        return False



def has_lowerC(psw):
    if any( char.islower() for char in psw):
        return True
    else :
        return False
    
def has_symbols(psw):
    if any((not char.isalnum()and char!=" ") for char in psw):
        return True
    else :
        return False


def has_upperC(psw):
    if any( char.isupper() for char in psw):
        return True
    else :
        return False

def matched_criterions(psw):
    nbr=0
    if has_digits(psw):
        nbr+=1
    if has_symbols(psw):
        nbr+=1
    if has_lowerC(psw):
        nbr+=1
    if has_upperC(psw):
        nbr+=1
    return nbr
    

def password_security(psw):
    leaked={"password123","openme1234",}
    score=matched_criterions(psw)
    if (len(psw)<8)or(psw.lower() in leaked):
        return "weak"
    elif ((score==1)or(score==0)or(score==2)):
        return "weak"
    elif(score==3):
        return "medium"
    elif (score==4):
        return "strong"

print (password_security("sir charji200")) 
