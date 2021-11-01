#output program jika n=4
print('output program jika n = 4:')
def starFormation1(n):
    for i in range(n):
        for j in range (i+1):
            print('*', end='')
        print()
n=4
starFormation1(n=4)


#output program jika n=4
print('output program jika n = 4:')
def starFormation2(n):
    for i in reversed(range(n)):
        for j in range(i+1):
            print('*', end='')
        print()
n=4
starFormation2(n=4)


#output program jika n =7
print('output program jika n = 7:')
def starFormation1(n):
    for i in range(n):
        for j in range (i+1):
            print('*', end='')
        print()

def starFormation2(n):
    for i in reversed(range(n)):
        for j in range(i+1):
            print('*', end='')
        print()

n=7
starFormation1(n-4)
starFormation2(n-3)
