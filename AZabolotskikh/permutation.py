class Premutation:
	def __init__(self, _):
		if len(set(_)) != len(_):
			raise Exception("not reversible")
		self._ = _
	def __eq__(self, _):
		return self._ == _._
	def __str__(self):
		return str(self._)
	def __mul__(self, other):
		if len(self._) != len(other._):
			raise Exception("Different arity")
		_ = [0] * len(self._)
		for i in range(len(self._)):
			_[i] = self._[other._[i] - 1]
		return Premutation(_)
	def printAsSubst(self):
		print ([i+1 for i in range(len(self._))])
		print (self)
	def __neg__(self):
		f = [0] * len(self._)
		for i in range(len(self._)):
			f[self._[i] -1]=i+1
		return f
	def __ne__(self,other):
		return not (self == other)
	def __pow__(self, i):
		this = self
		while i!=0:
			if i % 2 == 0:
				this *= this
				i /= 2
			else:
				this *= self
				i-=1
		return this 
	def parity(self):
		a = 0
		for j in range(len(self._)):
			for i in range(j):
				if self._[i] > self._[j]:
					a += 1
		return a%2==0
	def commutes(self, other):
		return self*other == other*self 

def main():
	a1 = Premutation([4,5,1,3,2])
	a2 = Premutation([2,3,4,5,1])
	print(a1*a2)
	print(a2*a1)
	for i in range(10):
		print (a1**(i+1))
		print (a2**(i+1))
	print ("inverse")
	print (-a1, -a2)
	print ("parity")
	print (a1.parity(), a2.parity())
	print ("equality")
	print(a1==a2)
	print ("commutes")
	print(a1.commutes(a2))
	print ("pow 10kkk")
	print(a1 ** (10**10), a2 ** (10**10))








main()