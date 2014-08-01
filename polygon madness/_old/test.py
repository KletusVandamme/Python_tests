class Test(object):
	def __init__ (self,x,y):
		self.x = x
		self.y = y
		self.z = 100
	def calc(self):
		self.z = self.x  + self.y
		return self.z

mytest = Test(3,10)
zzz = mytest.calc()
print zzz
print mytest.z