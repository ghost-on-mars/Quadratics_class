#march 27, 2026
import matplotlib.pyplot as plt
import numpy as np
import math
class quad:
    #constructer
    def __init__(self, a, b, c, h, k):
        self.a= a
        self.b=b
        self.c=c
        self.h=-b/(2*a)
        self.k=c-((b*b)/(4*a))

    #methods?
    def format(self, form, A, BH, CK,firstx, secondx):
        signh='+ '
        signk='+ '
        #if b or c are negative it changes to '' since the number
        #already has a - in it, otherwise it would print as h + -k
        if BH<0:
            signh= ''
        if CK<0:
            signk= ''
        return (form + str(A) + firstx + signh + str(BH) + secondx + signk + str(CK))

    def standard(self):
        return (self.format('standard form: y = ', self.a, self.b, self.c,'x² ', 'x '))

    def vertexform(self):
        return(self.format('vertex form: y = (', self.a, self.h, self.k,'x ', ')² '))

    def opening(self): 
        if self.a>0:
            return 'opens up'
        if self.a<0:
            return 'opens down'

    def vertex(self):
        vertexlist=[]
        #adds h and k to the list for the vertex
        vertexlist.append(self.h)
        vertexlist.append(self.k)
        return('vertex: ' +str(vertexlist).replace('[', '(').replace(']', ')'))

    def yint(self):
        #returns the y intercept
        return('y intercept: (0, ' + str(self.c) + ')')

    def xint(self):
        #!!!!ask if i need to make it return a list like the instructions say or if i can just have it return the nicely printed one
        xints= []
        #calculates the x intercepts
        try:
            self.x1=(-self.b + math.sqrt(self.b**2 - 4*self.a*self.c))/(2*self.a)
            self.x2=(-self.b - math.sqrt(self.b**2 - 4*self.a*self.c))/(2*self.a)
            xints.append(self.x1)
            if self.x1!=self.x2: #if theyre not the same, aka theres 2 xints
                #print('x intercepts: ('+ str(self.x1) + ', 0), ('+ str(self.x2) + ', 0)')
                xints.append(self.x2) #adds the second x int to the list
            #else:
                #print('x intercepts: ('+ str(self.x2) + ', 0)')
        except:
            #print('there are no x intercepts')
            return xints #returns an empty list
        return xints
        
    def addquad(self, a2, b2, c2):
        #adds the second quadratics and the first one, then returns the sum
        a3= a2 + self.a
        b3 = b2 + self.b
        c3 = c2 + self.c
        return self.format('sum of the quadratics: y = ', a3, b3, c3,'x² ', 'x ')
    
    def plot(self, a, b, c):
        #plots the quadratic
        def parabola(x,a,b,c):
            y = a*x**2 + b*x + c
            return y
        x = np.linspace(int(self.h)-5,int(self.h)+5,100)
        y = parabola(x,a,b,c) 
        plt.plot(x,y) #NEED THIS
        plt.plot(self.h, self.k, marker='o')
        plt.axhline(y=0, color='black', linestyle='-')
        plt.axvline(x=0, color='black', linestyle='-')
        plt.text(self.h-0.5, self.k-2, 'vertex: (' + str(self.h) +', ' + str(self.k) + ')',color='green', fontsize=9)
        plt.plot(0, c, marker="o", color='purple') #y int
        plt.text(-0.5, c-2, 'y int: (0, ' + str(c) + ')',color='purple', fontsize=9)
        plt.plot(self.h, self.k, marker="o",color='green') #vertex
        if len(self.xint())>1: #if theres more than one x int it adds them on the plot. if theres only one its just the vertex
            plt.plot(self.xint()[0], 0, marker="o", color='red')
            plt.plot(self.xint()[1], 0, marker="o", color='blue')
            plt.text(self.xint()[0]+0.5, -2, 'x int: ('+ str(self.xint()[0]) + ', 0)',color='red', fontsize=9)
            plt.text(self.xint()[1]-2, -2, 'x int: ('+ str(self.xint()[1]) + ', 0)',color='blue', fontsize=9)
        plt.show()
        inputloop() #goes back to the input loop

A=int(input('A value:'))
B=int(input('B value:'))
C=int(input('C value:'))
q1=quad(A, B, C, 0, 0) #the 0s are just placeholders
updated=0

def inputloop():
    global updated
    if updated==0: #used updated so it just prints out the options if its the first loop
        whichinfo=input('\nenter the number of the action you would like to take, or x to quit\n'
        '1: display the standard form\n2: display the vertex form\n3: display the direction of '
        'opening\n4: display the vertex coordinates\n5: display the y intercept\n6: display the'
        ' x intercepts\n7: add another quadratic\n8: plot the graph\n')
    else: #otherwise it just says to enter the number
        whichinfo=input('enter the number of the action you would like to take, or x to quit\n')
    updated=1
    if whichinfo.upper()=='X': #i did upper() so both x and X work.
        print('goodbye!')
        exit()
    while True:
        try:
            #tries converting whichinfo to an int. i did this now instead of whichinfo=int(input())
            #so x can be input without getting an error from it being a string
            whichinfo=int(whichinfo)
            if whichinfo not in range(1,9): #also if its an int it checks if its in the range
                print('not in range')
                inputloop()
            break
        except ValueError:
            print('invalid input')
            inputloop()

    if whichinfo==7: #if its to add a qquadratic
        A2=int(input('A value of quadratic to add:'))
        B2=int(input('B value of quadratic to add:'))
        C2=int(input('C value of quadratic to add:'))
        print(q1.addquad(A2, B2, C2))
    elif whichinfo==8: #if 
        q1.plot(A, B, C)
    else: #if its anything else does it
        functionlist=[q1.standard, q1.vertexform, q1.opening, q1.vertex, q1.yint, q1.xint]
        print(functionlist[whichinfo-1]())#(A, B, C)
    inputloop() #loops so you can continue 

inputloop()