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
		

def get_user_input():
	print("Please input data...")
	id = str(input('School ID: '))
	name = str(input('Name School: '))
	if len(name) <= 3:
		print('Name must have more than 3 characters')
		return None
	address = str(input('Address: '))
	return Schools(name, address, id)

if __name__ == '__main__':
	while True:
		school = get_user_input()
		if school:
			school.save()
		play_again = input("Press 'n' to stop, other to continue: ")
		if play_again == 'n' or play_again == "N":
			break




