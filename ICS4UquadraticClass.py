import math
vertexlist=[]
xintlist=[]
class quad:
    #constructer
    def __init__(self, a, b, c):
        self.a= a
        self.b=b
        self.c=c
    #methods?
    def standard(self, a, b, c):
        signh='+ '
        signk='+ '
        #if b or c are negative it changes to '' since the number
        #already has a - in it, otherwise it would print as h + -k
        if b<0:
            signh= ''
        if c<0:
            signk= ''
        print('standard form: y = ' + str(a) + 'x² ' + signh + str(b) + 'x ' + signk + str(c))

    def vertexform(self, a, b, c):
        h=(b*-1)/(2*a)
        k=c-((b*b)/(4*a))
        #by default it will put + between the numberes
        signh='+ '
        signk= '+ '
        if h<0:
            signh= ''
        if k<0:
            signk= ''
        print('vertex form: y = (' + str(a) + 'x ' + signh + str(h) + ')² ' + signk + str(k))

    def opening(self, a, b, c): #b and c arent used, but since functionlist[whichinfo-1](A, B, C) has
        #B and C, i included b and c here so i didnt have to make a seperate thing for if whichinfo==3
        if a>0:
            print('opens up')
        if a<0:
            print('opens down')

    def vertex(self, a, b, c):
        #calculates the vertex and adds to a list, then prints it
        h=(b*-1)/(2*a)
        k=c-((b*b)/(4*a))
        vertexlist.append(h)
        vertexlist.append(k)
        print('vertex:', str(vertexlist).replace('[', '(').replace(']', ')'))

    def yint(self, a, b, c):#dont need a and b, but i kept them for the same reason as with opening
        #prints the y intercept
        print('y intercept: (0, ' + str(c) + ')')

    def xint(self, a, b, c):
        #NEED TO MAKE IT RETURN A LIST????????????????
        #xintlist.append()
        if ((b*b)-4*a*c)<0:
            print('there are no real roots')
        elif ((b*b)-4*a*c)==0:
            h=str((b*-1)/(2*a))
            k=str(c-((b*b)/(4*a)))
            print('x intercept: ('+h+', '+k+')')
           
        else:
            x1=(b*-1) + math.sqrt((b*b)+(-4*a*c))
            x1=x1/(2*a)
            x2=(b*-1) - math.sqrt((b*b)+(-4*a*c))
            x2=x2/(2*a)
            xintlist.append('('+str(x1)+', 0)')
            xintlist.append('('+str(x2)+', 0)')
            print('x intercept:', *xintlist)
            
    def addquad(self, a2, b2, c2, a, b, c):
        #adds the second quadratics and the first one, then prints the sum
        a3= a2 + a
        b3 = b2 + b
        c3 = c2 + c
        signh='+ '
        signk='+ '
        if b3<0:
            #b3='- ' + str(b3*-1) #times b3 by -1 to convert it to positive, and adds '- ' so it prints as '- b3'
            signh= ''
        if c3<0:
            signk= ''
        print('sum of the quadratics: y = ' + str(a3) + 'x² ' + signh + str(b3) + 'x ' + signk + str(c3))

A=int(input('A value:'))
B=int(input('B value:'))
C=int(input('C value:'))
q1=quad(A, B, C)

updated=0

def inputloop():
    global updated
    if updated==0: #if its the first loop it prints out the options
        whichinfo=input('\nenter the number of the action you would like to take, or x to quit\n'
        '1: display the standard form\n2: display the vertex form\n3: display the direction of '
        'opening\n4: display the vertex coordinates\n5: display the y intercept\n6: display the'
        ' x intercepts\n7: add another quadratic\n')
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
            if whichinfo not in range(1,8): #also if its an int it checks if its in the range
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
        q1.addquad(A2, B2, C2, A, B, C)
    else:
        functionlist=[q1.standard, q1.vertexform, q1.opening, q1.vertex, q1.yint, q1.xint]
        functionlist[whichinfo-1](A, B, C)
    inputloop() #loops so you can continue to choose information about the quadratic

inputloop()
