import os
school_txt = os.path.join(os.getcwd(), 'datas/schools.txt')

id = 0

class Schools(object):

    def __init__(self,name = None,address = None,id = 0):
        self.id = id
        self.name = name
        self.address = address


    def save(self):
        f = open('schools.txt','w')
        self.id +=1
        f.write('{},{},{}'.format(self.id,self.name, self.address))
        f.close()

    def get_with_id(self,school_id):
    	file = open(school_txt,'r')
    	for line in file.readlines():
    		datas = lines.split(',')
    		if int(datas[0] == school_id):
    			self.id = school_id
    			self.name = datas[1]
    			self.address = datas[2]
    		return self
    	return None

