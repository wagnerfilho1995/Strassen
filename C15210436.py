# encoding: utf-8
# Deve conter o método Strassen

import math

def maiorInteiro(x):
    x = math.ceil(math.log2(x))
    return 2**x

def multiplique2x2(X, Y):
    Z = [[0 for j in range(0, len(X))]for i in range(0, len(X))]
    for i in range(len(X)):
        for j in range(len(X)):
            for k in range(len(X)):
                Z[i][j] += X[i][k] * Y[k][j]
    return Z

def some(X, Y):
    S = [[0 for j in range(0, len(X))]for i in range(0, len(X))]
    for i in range(0, len(X)):
        for j in range(0, len(X[0])):
            S[i][j] = X[i][j] + Y[i][j]
    return S

def subtraia(X, Y):
    S = [[0 for j in range(0, len(X))]for i in range(0, len(X))]
    for i in range(0, len(X)):
        for j in range(0, len(X[0])):
            S[i][j] = X[i][j] - Y[i][j]
    return S

def bunito(A, B):
    tam = len(A)
    if tam <= 2: # Caso Base
        #   Faça a multiplicação!!
        return multiplique2x2(A, B)
    else:
        novoTamanho = int(tam/2)
        #   Inicialize as 4 submatrizes que apareçem ao fazer a divisão de A
        subA11 = [[0 for j in range(0, novoTamanho)]for i in range(0, novoTamanho)]
        subA12 = [[0 for j in range(0, novoTamanho)]for i in range(0, novoTamanho)]
        subA21 = [[0 for j in range(0, novoTamanho)]for i in range(0, novoTamanho)]
        subA22 = [[0 for j in range(0, novoTamanho)]for i in range(0, novoTamanho)]

         #   Inicialize as 4 submatrizes que apareçem ao fazer a divisão de B
        subB11 = [[0 for j in range(0, novoTamanho)]for i in range(0, novoTamanho)]
        subB12 = [[0 for j in range(0, novoTamanho)]for i in range(0, novoTamanho)]
        subB21 = [[0 for j in range(0, novoTamanho)]for i in range(0, novoTamanho)]
        subB22 = [[0 for j in range(0, novoTamanho)]for i in range(0, novoTamanho)]

        #   Atribua corretamente o conteudo dos 4 quadrantes de A e B nas submatrizes inicializadas
        for i in range(0, novoTamanho):
            for j in range(0, novoTamanho):
                subA11[i][j] = A[i][j]                           #   Segundo quadrante de A (Cima - Esquerda)
                subA12[i][j] = A[i][j+novoTamanho]               #   Primeiro quadrante de A (Cima - Direita)
                subA21[i][j] = A[i+novoTamanho][j]               #   Terceiro quadrante de A (Baixo - Esquerda)
                subA22[i][j] = A[i+novoTamanho][j+novoTamanho]   #   Quarto quadrante de A (Baixo - Direita)

                subB11[i][j] = B[i][j]                           #   Segundo quadrante de B (Cima - Esquerda)
                subB12[i][j] = B[i][j+novoTamanho]               #   Primeiro quadrante de B (Cima - Direita)
                subB21[i][j] = B[i+novoTamanho][j]               #   Terceiro quadrante de B (Baixo - Esquerda)
                subB22[i][j] = B[i+novoTamanho][j+novoTamanho]   #   Quarto quadrante de B (Baixo - Direita)

        #   Crie duas Matrizes para representar a solução de cada operação nas submatrizes de A e de B
        solA = [[0 for j in range(0, novoTamanho)]for i in range(0, novoTamanho)]
        solB = [[0 for j in range(0, novoTamanho)]for i in range(0, novoTamanho)]

        #   Agora calcule os 7 produtos!

        ##   P1 = (subA11 + subA22) * (subB11 + subB22)  ##
        solA = some(subA11, subA22) # A11 + A22
        solB = some(subB11, subB22) # B11 + B22
        P1 = bunito(solA, solB) # (A11+A22) * (B11+B22)
       
        ##  P2 = (subA21 + subA22) * subB11 ##
        solA = some(subA21, subA22) # A21 + A22
        P2 = bunito(solA, subB11) # (A21+A22) * B11

        ##  P3 = (subA11) * (subB12 - subB22) ##
        solB = subtraia(subB12, subB22)
        P3 = bunito(subA11, solB)

        ##  P4 = (subA22) * (subB21 - subB11) ##
        solB = subtraia(subB21, subB11)
        P4 = bunito(subA22, solB)

        ##  P5 = (subA11 + subA12) * subB22 ##
        solA = some(subA11, subA12)
        P5 = bunito(solA, subB22)

        ##  P6 = (subA21 - subA11) * (subB11 + subB12) ##
        solA = subtraia(subA21, subA11)
        solB = some(subB11, subB12)
        P6 = bunito(solA, solB)

        ##  P7 = (subA12 - subA22) * (subB21 + subB22) ##
        solA = subtraia(subA12,subA22)
        solB = some(subB21, subB22)
        P7 = bunito(solA, solB)

        #   Agora calcule os elementos da matrix resposta C
        c12 = some(P3, P5)
        c21 = some(P2, P4)

        solA = some(P1, P4)
        solB = some(solA, P7)
        c11 = subtraia(solB, P5)

        solA = some(P1, P3)
        solB = some(solA, P6)
        c22 = subtraia(solB, P2)

        C = [[0 for j in range(0, tam)]for i in range(0, tam)]
        for i in range(0, novoTamanho):
            for j in range(0, novoTamanho):
                C[i][j] = c11[i][j]
                C[i][j + novoTamanho] = c12[i][j]
                C[i+novoTamanho][j] = c21[i][j]
                C[i+novoTamanho][j+novoTamanho] = c22[i][j]
        return C

def Strassen( matrix1 , matrix2 ):

    #   Definir o tamanho das matrizes que serão trabalhadas (Para que sejam quadradas e com dimensões em potência de 2)
    novoTamanho = maiorInteiro(max(len(matrix1[0]),len(matrix1), len(matrix2[0]), len(matrix2)))
    
    #   Criar matrizes A e B inicialmente todas preenchidas com 0
    A = [[0 for j in range(novoTamanho)]for i in range(novoTamanho)]
    B = [[0 for j in range(novoTamanho)]for i in range(novoTamanho)]

    #   Ocupar as posições ij, correspondentes de matrix1 e matrix2, nas posições ij de A e B
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix1[0])):
            A[i][j] = matrix1[i][j]
    for i in range(0, len(matrix2)):
        for j in range(0, len(matrix2[0])):
            B[i][j] = matrix2[i][j]
    
    #   Chame o strassen!
    matrix3 = bunito(A, B)
   
    return matrix3

def readFiles( name_m1 , name_m2 ):

    matrix1 = []
    matrix2 = []

    readM1 = open(name_m1, 'r')
    lineM1, rowM1 = map( int, readM1.readline().split() )
    for i in range(lineM1):
        matrix1 +=  [list(map( int, readM1.readline().split() ))]

    readM2 = open(name_m2, 'r')
    lineM2, rowM2 = map( int, readM2.readline().split() )
    for i in range(lineM2):
        matrix2 +=  [list(map( int, readM2.readline().split() ))]

    readM2.close()
    readM1.close()

    return matrix1 , matrix2

m1 , m2 = readFiles( 'M1.in' , 'M2.in' )

print( Strassen(m1,m2) )