import rich
#the check functions
def has_lowerC(psw):
    return any( char.islower() for char in psw)

def has_digits(psw):
    return any(char.isdigit() for char in psw)  

def has_symbols(psw):
    return any((not char.isalnum()) for char in psw)

def has_upperC(psw):
    return any( char.isupper() for char in psw)

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
    leaked={"password123",
    "openme1234",
    "qwerty123",
    "letmein123",
    "welcome123",
    "admin1234",
    "iloveyou123",
    "123456789",
    "password1",
    "changeme123",}
    score=matched_criterions(psw)
    if (len(psw)<8)or (psw.lower() in leaked) or (" " in psw):
        return "[bold red]weak[bold red]"
    elif ((score==1)or(score==0)or(score==2)):
        return "[bold red]weak[bold red]"
    elif(score==3):
        return "[yellow]medium[yellow]"
    elif (score==4):
        return "[green]strong[green]"


mdp=input ("entrez le mot de passe ")
console.print (password_security(mdp)) 
