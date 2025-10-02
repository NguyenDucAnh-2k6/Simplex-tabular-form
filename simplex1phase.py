import sys
from fractions import Fraction
def Input():
    f=sys.stdin
    [n,m]=[int(x) for x in f.readline().split()]
    C=[-float(x) for x in f.readline().split()]
    A=[]
    for i in range(m):
        row=[float(x) for x in f.readline().split()]
        A.append(row)
    b=[float(x) for x in f.readline().split()]
    return n,m,C,A,b
def inputfile(filename):
    with open(filename, 'r') as f:
        [n,m]=[int(x) for x in f.readline().split()]
        c=[-float(x) for x in f.readline().split()]
        A=[]
        for i in range(m):
            row=[float(x) for x in f.readline().split()]
            A.append(row)
        b=[float(x) for x in f.readline().split()]
    return n,m,c,A,b        
n,m,c,A,b=Input()
#n,m,c,A,b=inputfile('datasimplex.txt')
def simplex(c,A,b):
    m,n=len(A),len(A[0])
    tableau=[row + [0]*m+[b[i]] for i,row in enumerate(A)]
    #Adding objective row
    tableau.append(c+[0]*(m+1))
    #Slack vars
    for i in range(m):
        tableau[i][n+i]=1
    basic_vars=list(range(n,n+m))
    non_basic_vars=list(range(0,n))
    def print_tableau():
        for row in tableau:
            print(Fraction(x).limit_denominator() for x in row)
        print()
    #print('Initial tableau: ')
    #print_tableau()
    #Simplex
    while any(x<0 for x in tableau[m][:-1]):
        pivot_col=min((j for j in range(n+m)), key=lambda j: tableau[-1][j])
        ratios=[]
        for i in range(m):
            if tableau[i][pivot_col]>0:
               ratios.append((tableau[i][-1]/tableau[i][pivot_col],i))
        if not ratios:
            raise ValueError('UNBOUNDED')
        pivot_row=min(ratios)[1]  #Need look back
        pivot_element=tableau[pivot_row][pivot_col]
        tableau[pivot_row]=[x/pivot_element for x in tableau[pivot_row]]   #Normalize pivot_row
        for i in range(m+1):     #All rows, gaussian
            if i!=pivot_row:
                factor=tableau[i][pivot_col]
                tableau[i]=[tableau[i][j]-factor*tableau[pivot_row][j] for j in range(n+m+1)]
        basic_vars[pivot_row]=pivot_col   #Switch basic variables
        #print('Updated Tableau: ')
        #print_tableau()
    #Extract final solution
    x=[0]*n
    for i in range(m):
        if basic_vars[i]<n:   #Just care about original variables
            x[basic_vars[i]]=tableau[i][-1]
    return tableau[-1][-1], x
optimal_val, x=simplex(c,A,b)
print(n)
for i in range(n):
    print(x[i], end=' ')
def add(x,y):
    return x+y
    
    
        
        
            
            
            
        
        
    

        
