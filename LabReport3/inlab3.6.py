class node:
    def __init__(self, co =None, exp=None):
        self.co = co
        self.exp = exp
        self.next = None

p1=None
p2=None
Sum=None

def create(head, co, exp):
    if head==None:
        temp=node(co, exp)
        head=temp
    else:
        temp=head
        while temp.next != None:
            temp=temp.next
        flag=node(co, exp)
        temp.next=flag
        return head

def polyAdd(p1, p2, Sum):
    poly1 = p1
    poly2 = p2

    if poly1 != None and poly2 == None:
        Sum=poly1
        return Sum

    elif poly1 == None and poly2 == None:
        Sum=poly2
        return Sum

    while poly1 != None and poly2 == None:

        if Sum == None:
            Sum = node()
        Res = Sum

    else:
        Res.next = node()
        Res = Res.next

    if poly1.exp > poly2.exp:
        Res.co = poly1.co
        Res.exp = poly1.exp
        poly1 = poly1.next

    elif poly1.exp < poly2.exp:
        Res.co = poly2.co
        Res.exp = poly2.exp
        poly2=poly2.next

    elif poly1.exp == poly2.exp:
        Res.co = poly1.co + poly2.co
        Res.exp = poly1.exp
        poly1 = poly1.next
        poly2 = poly2.next

    while poly1 != None:
        Res.next = node()
        Res = Res.next
        Res.co = poly1.co
        Res.exp = poly1.exp
        poly1 = poly1.next

    while poly2 != None:
        Res.next = node()
        Res = Res.next
        Res.co = poly2.co
        Res.exp = poly2.exp
        poly2 = poly2.next

        Res.next = None

        return Sum

def display(poly):
    temp=poly
    while temp != None:
        print(temp.co, '^',temp.exp,'+', end = '')
        temp=temp.next
        print()

loop = True

while loop:
    print('1. Enter Polynomial 1')
    print('2. Enter Polynomial 2')
    print('3. Perform addition')
    print('5. Exit')
    break

    ch = int(int())

    if ch == 1:
        co = int(input('Enter co-efficient\n'))
        exp = int(input('Enter exponent\n'))

        p1 = create(p1, co, exp)

    elif ch == 2:
        co = int(input('Enter co-efficient\n'))
        exp = int(input('Enter exponent\n'))

        p2 = create(p2, co, exp)

    elif ch == 3:
        Sum = polyAdd(p1, p2, Sum)
        print('\nPolynomial 1')
        display(p1)
        print('\nPolynomial 2')
        display(p2)
        print('\nSum:' )
        display(Sum)

    elif ch == 4:
        loop = False

    else:
        print('Wrong Choice! Re-enter')