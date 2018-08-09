import os
school_txt = os.path.join(os.getcwd(), 'datas/schools.txt')

id = 0

class Schools(object):

	def __init__(self,name = None,address = None,id = 0):
		self.name = name
		self.address = address
		self.id = id

	def save(self):
		f = open('schools.txt','w')
		id +=1
		f.write({},{},{}.format(self.name, self.address,self.id))
		f.close()
	def get_with_id(self,school_id):
		files = open(school_txt,'r')
		for line in files.readlines():
			datas = lines.split(',')
			if int(datas[0] == school_id):
				self.id = school_id
				self.name = datas[1]
				self.address = datas[2]
			return self
		return None
		

	def get_user_input(id=0):
		print("Please input data: ")
		name = str(input('Name: '))
		if len(name) <= 3:
			print('Name must have more than 3 characters')
			return None
		address = str(input('Address: '))
		return Schools(name, address, id)





