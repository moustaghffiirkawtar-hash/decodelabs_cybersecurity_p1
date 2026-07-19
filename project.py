import rich
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
console= Console()
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
        return "weak"
    elif ((score==1)or(score==0)or(score==2)):
        return "weak"
    elif(score==3):
        return "medium"
    elif (score==4):
        return "strong"
    
def show_checklist(psw):
    table = Table(title="Criteria Check")
    table.add_column("Criterion")
    table.add_column("Status")

    table.add_row("Digit", "✓" if has_digits(psw) else "✗")
    table.add_row("Uppercase", "✓" if has_upperC(psw) else "✗")
    table.add_row("Lowercase", "✓" if has_lowerC(psw) else "✗")
    table.add_row("Symbol", "✓" if has_symbols(psw) else "✗")

    console.print(table)

def show_verdict(result):
    colors = {"weak": "red", "medium": "yellow", "strong": "green"}
    console.print(Panel(f"Password strength: {result.upper()}", style=f"bold {colors[result]}"))

console.print(Panel("Create a password", style="bold cyan"))
mdp = input("Enter your password: ")

show_checklist(mdp)
result = password_security(mdp)
show_verdict(result)