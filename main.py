def is_palindrome(n):#problema 5
    '''
    determinam daca un numar este palindrom sau nu
    :param n: numarul pe care il verificam daca este palindrom sau nu
    :return: bool: True daca numarul este palindrom sau False in caz contrar
    '''

    x=n
    r=0
    while n:
        c=x%10
        r=r*10+c
        x=x//10
    if x==r:
        return True
    else:
        return False
def test_is_palindrome():
    assert(is_palindrome(121))==True
    assert(is_palindrome(233))==False

def is_prime(n):#problema 6
    '''
    verificam daca un numar dat este prim sau nu
    :param n: numarul pe care il verificam daca este prim sau nu
    :return:bool: True daca numarul pe care il verificam este prim sau False in caz contrar
    '''
    if n<2:
        return False
    if n==2:
        return True
    for i in range(3,n//2,2):
        if n%i==0:
            return False
        else:
            return True
def is_superprime(n):
    '''
    verificam daca un numar este superprim sau nu
    :param n: numarul pe care il verificam daca este superprim sau nu
    :return: bool: True daca numarul este superprim sau False in caz contrar
    '''
    x=n
    while x:
        if is_prime(x)==False:
            return False
        x=x//10
    return True
def test_is_superprime():
    assert(is_superprime(233))==True
    assert(is_superprime(237))==False

def get_largest_prime_below(n):#problema 1
    run=False
    '''
    gasim ultimul numar prim mia mic decat numarul n dat
    :param n:numarul de la care pornim sa cautam numarul prim dinaintea lui
    :return: ulrimul numar prim mai mic decat n
    '''

    while run==False:
        for i in range(n-1,1,-1):
            if is_prime(i)==True:
                run=True
                return i
def test_get_largest_prime_below():
    assert(get_largest_prime_below(15))==13
    assert(get_largest_prime_below(9))==7

def main():
    shouldRun==True
    while shouldRun:
        print('1.numarul dat este palindrom sau nu')
        print('2.numarul dat este superprim sau nu')
        print('3.ultimul numar prim mai mic decat numarul citit')
        print('4.iesire')
        optiune=input('Dati optiune:')
        if optiune=='1':
            n=int(input('Dati numarul:'))
            if is_palindrome(n)==True:
                print('numarul dat este palindrom')
            else:
                print('numarul dat nu este palindrom')
        elif optiune=='2':
            n=int(input('Dati numarul:'))
            if is_superprime(n)==True:
                print('numarul este superprim')
            else:
                print('numarul nu este superprim')
        elif optiune=='3':
            n=int(input('dati numarul:'))
            print(get_largest_prime_below(n))
        elif optiune=='4':
            shouldRun==False
main()