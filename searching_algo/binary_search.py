
#--------------iteration algo------------------

N = [i for i in range(100)]

def binary_s(N, A):

    M = 0
    while M != A:
        n = len(N)//2
        M = N[n]
        N_left, N_right = N[:n], N[n+1:] # постоянно забываю что сюда передаем не переменную, а ее положение в списке

        if A == M:
            print("I found it!!")
        elif A > M:
            N = N_right[:]
            #binary_s(N,A)
        elif A < M:
            N = N_left[:]
            #binary_s(N, A)

binary_s(N, 30)

#----------------------------------------------------------------------------------
#-------------------with recursion-------------------------------------------------
#----------------------------------------------------------------------------------

N = [i for i in range(100)]

def binary_s(N, A):

    n = len(N)//2
    M = N[n]
    N_left, N_right  = N[:n], N[n+1:]

    if A == M:
        print("I found it!! with recursion")
    elif A > M:
        N = N_right[:]
        binary_s(N,A)
    elif A < M:
        N = N_left[:]
        binary_s(N, A)

binary_s(N, 99)