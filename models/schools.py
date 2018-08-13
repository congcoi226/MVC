import os
school_txt = os.path.join(os.getcwd(), 'datas/schools.txt')



class Schools(object):

	def __init__(self,name = None,address = None,id = 0):
		self.name = name
		self.address = address
		self.id = id

	def save(self):
		f = open('schools.txt','w')
		f.close()
		return None
		

	def get_datas_input(self):
		print("Please input school datas...")
		id = str(input('School ID: '))
		name = str(input('Name School: '))
		if len(name) <= 3:
			print('Name must have more than 3 characters')
			return None
		address = str(input('Address: '))
		return Schools(name, address, id)





