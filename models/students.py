import os

student_txt = os.path.join(os.getcwd(), 'datas/students.txt')

id = 0

class Students(object):

    def __init__(self,name = None,address = None,id = 0):
        self.name = name
        self.address = address
        self.id = id

    def save(self):
        f = open('students.txt','w')
        id +=1
        f.write({},{},{}.format(self.name, self.address,self.id))
        f.close()
    def get_with_id(self, student_id):
    	files =  open(student_txt,'r')
    	for line in files.readlines():
    		datas = lines.split(',')
    		if int(data[0]) == student_id:
    			self.id = student_id
    			self.name = data[1]
    			self.address = data[2]
    		return self
    	return None

