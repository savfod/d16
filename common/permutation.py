class Permutation:
 	def __init__(self,A):
 		self.A=A
 	def f(self,n):
 		return self.A[n-1]
 	def f_(self,n):
 		for i in range(len(self)):
 			if self.f(i)==n:
 				return i
 	def __str__(self):
 		return (str(self.A))
 	def __len__(self):
 		return len(self.A)
 	def __mul__(X,Y):
 		A=[]
 		for i in range(1,len(X)+1):
 			A.append(X.f(Y.f(i)))
 		return Permutation(A)
 	def __pow__(X,n):
 		if n==-1:
 			A=[i for i in range(len(X))]
 			for i in range(0,len(X)):
 				A[i]=X.f_(i+1)
 			return Permutation(A)
 		if n==1:
 			return X
 		if n%2==0:
 			return (X*X)**(n//2)
 		else:
 			return X**(n-1)*X
 	def conjugation(self,other):
 		return self**-1*other*self
a1=Permutation([4,5,1,3,2])
a2=Permutation([2,3,4,5,1])
print(a1**-1)
