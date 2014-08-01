# build 2d array
# from numpy *
from matt_stuff import *


class My_array(object):
	def __init__ (self, twod_array):
		self.twod_array = twod_array
		self.a = 99
	def get_row (self,row):
		output = []
		return self.twod_array[row]

	def get_col (self,col):
		self.col = col
		output = []
		for i in range (0,len(self.twod_array)):
			output.append(array_of_rows[i][4])
		return output
	def print_col (self,col):
		self.col = col
		output = []
		sep()
		print "here is column", self.col
		for i in range (0,len(self.twod_array)):
			print array_of_rows[i][4]

	def print_2d(self):
		#print array in 2d
		sep()
		print "here is your array in 2d format"
		for i in range (0,len(self.twod_array)):
			print self.twod_array[i]
	def get_element(self, (x,y)):
		sep()
		print "here is element (", x, ",", y,")"
		print self.twod_array[x][y]
		return self.twod_array[x][y]





num_row = 3
num_col = 5
array_of_rows = []
array_of_elements =[]

#create array
# for each row
for x in range (0,num_row):
	array_of_elements = []
	for y in range (0,num_col):
		array_of_elements.append((x,y))
	array_of_rows.append(array_of_elements)

my_array = My_array(array_of_rows)
my_array.print_2d()
my_array.print_col(3)
my_array.get_element((2,4))

sep()
print "returned column"
print my_array.get_col(0)

sep()
print "returned row"
print my_array.get_row(1)


# new_array = [[3]*num_col]*num_row
# new_array[2][2] = (6,6)

# sep()
# print "new array"
# print new_array

