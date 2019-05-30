# -*- coding: utf-8 -*-

class Matrix:
        def __init__(self,row=2,col=2,elementlists=[1,2,3,4]):
            if len(elementlists) == row*col:
                self.__row=row
                self.__col=col
                self.__Matrix = []
                m=0
                x=col
                for i in range(self.__row):
                    self.__Matrix.append(elementlists[m:x])
                    m+=col
                    x+=col
            else:
                print("--Try again-- Please control your matrix entries!!")

        def get_rowdim(self):
            return self.__row
        def get_coldim(self):
            return  self.__col

        def get_Matrix(self):
            return self.__Matrix

        def get_MatrixElement(self,i,j):
             return  self.__Matrix[i][j]

        def insert_row(self,rowNumber = [1,5],rowlist=[1,2,3]):

                if isinstance(rowNumber,int):
                    if len(rowlist)==self.__col:
                        self.__Matrix.insert(rowNumber-1,rowlist)
                        self.__row+=1
                        return self.__Matrix
                    else:
                        print("--Try again--Your list is not same column dimension!!")

                if isinstance(rowNumber,list):
                    if len(rowNumber)==len(rowlist):
                        c=0
                        for k in range(len(rowNumber)):
                            if isinstance(rowlist[k],list) and len(rowlist[k])==self.__col:
                                c=c+1
                        if  c == len(rowNumber):
                            for i in range(len(rowNumber)):
                                self.__Matrix.insert(rowNumber[i]-1,rowlist[i])
                                self.__row+=1
                            return self.__Matrix
                        else:
                            print("--Try again--Your list is not same column dimension!!")
                    else:
                        print("--Try again--Your list is not same column dimension!!2")

        def delete_row(self,rowNumber=[]):
            if isinstance(rowNumber,int):
                self.__Matrix.pop(rowNumber-1)
                self.__row-=1
                return self.__Matrix
            if isinstance(rowNumber,list):
                for i in range(len(rowNumber)):
                    self.__Matrix.pop(rowNumber[i]-1)
                    self.__row-=1
                return self.__Matrix


        def set_MatrixElement(self,i,j,value):
            self.__Matrix[i][j]=value

        def Transpoze(self):
            self.__Matrix = [[self.__Matrix[j][i] for j in range(len(self.__Matrix))]for i in range(len(self.__Matrix[0]))]
            return self.__Matrix

        def Trace(self):
            sum=0
            if self.__col==self.__row:
                for i in range(len(self.__Matrix)):
                    for j in range(len(self.__Matrix)):
                        if  i==j:
                            sum+=self.__Matrix[i][j]
                return sum
            else:
                return print("This is not square matrix!")

        def Multiply(self,A):
            if isinstance(A,int):
                self.__Matrix = [[(self.__Matrix[i][j])*A for j in range(len(self.__Matrix[0]))] for i in range(len(self.__Matrix))]
                return self.__Matrix
            if isinstance(A,list):
                sum=0
                result=list()
                result_row=list()
                if len(self.__Matrix[0])==len(A):
                    for i in range(len(self.__Matrix)):
                        for j in range(len(A[0])):
                            for k in range(len(self.__Matrix[0])):
                                sum += self.__Matrix[i][k]*A[k][j]
                            result_row.append(sum)
                            sum=0
                        result.append(result_row)
                        result_row=list()
                    return result
                else:
                   return print ("No Solution")
            else:
                print("Get Matrix or int!!")

        @staticmethod
        def determinant(A):
            total=0
            if len(A)==2 and len(A[0])==2:
                val = ((A[0][0]) * (A[1][1])) - ((A[1][0]) * (A[0][1]))
                return val
            for j in range(len(A)):
                a = A
                a = a[1:]
                for i in range(len(a)):
                    a[i] = a[i][0:j] + a[i][j+1:]
                sign = (-1) ** (j % 2)
                sub_det = Matrix.determinant(a)
                total += sign * (A[0][j]) * sub_det
            return total

        @staticmethod
        def copy(A):
            n=len(A)
            m=len(A[0])
            B=[[0 for j in range(m)]for i in range(n)]
            for k in range(n):
                for t in range(m):
                    B[k][t]= A[k][t]
            return B

        def Inverse(self):
            A=Matrix.copy(self.__Matrix)
            if self.__row==self.__col and Matrix.determinant(A)!=0:
                row = len(A)
                r =list(range(row))
                Id = [[0 for j in range(row)] for i in range(row)]
                for i in range(row):
                    for j in range(len(A[0])):
                        if i == j:
                            Id[i][j] = 1
                        else:
                            Id[i][j] = 0
                for i in range(row):
                    m=1.0/A[i][i]
                    for j in range(row):
                        Id[i][j]*=m
                        A[i][j]*=m
                    for k in r[0:i] + r[i+1:]:
                        rw=A[k][i]
                        for l in range(row):
                            A[k][l] = A[k][l] - rw*A[i][l]
                            Id[k][l] = Id[k][l] - rw*Id[i][l]
                return Id
            else:
                return print("Not Inversible!!")
















