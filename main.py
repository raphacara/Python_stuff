from random import randint
from math import sqrt

def echange(x,y):
    """Echange les valeurs x et y"""
    z=x
    x=y
    y=z
    return(x,y)
#On peut faire la même chose avec la commande x,y=y,x

def IMC(poids,taille):
    """Calcule l'IMC"""
    z=poids/taille**2
    return(z)

def minimum(a,b):
    """retourne le miniimum entre a et b"""
    if a>b:
        return(b)
    return(a)
#la fonction existe déjà et c'est min

def parite(n):
    """retourne si n est pair"""
    return(n%2==0)
#retourne ici un booléen

def multiple(a,b):
    """retourne si a est un multiple de b"""
    return(a%b==0)
    
def plusoumoins():
    """jeu du plus ou moins"""
    x=randint(0,1000)
    t=-1
    while x!=t:
        print("Devine le nombre:")
        t=input()
        t=int(t)                 #on transforme t de caractère à nombre
        if x>t:
            print("C'est plus !")
        if x<t:
            print("C'est moins !")
    return("C'est gagné ! Bravo !")
    
def resolution(a,b,c):
    """résolution de l'équation ax^2+bx+c=0"""
    D=b**2-4*a*c
    if D<0:
        return("L'équation n'a pas de solutions")
    if D==0:
        return(-b/(2*a))
    if D>0:
        x1=(-b+sqrt(D))/(2*a)
        x2=(-b-sqrt(D))/(2*a)
        return(x1,x2)
        
def racine(a,n=10):
    """approxime la valeur de la racine de a avec n itérations"""
    u=1
    for i in range(1,n+1):
        u=0.5*(u+a/u)
    return(u)
    
def modulo(x,n):
    """retourne x modulo n"""
    if x<0:
        while x<0:
            x=x+n
        return(x)
    if x>=0 and x<n:
        return(x)
    if x>0:
        while x>=0:
            x=x-n
        return(x+n)
