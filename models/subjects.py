import os

subject_txt = os.path.join(os.getcwd(), 'datas/subjects.txt')
student_txt = os.path.join(os.getcwd(), 'datas/students.txt')
id = 0
class Subjects(object):
	def __init__(self, name = None, id = 0,student_id = 0):
		self.name = name
		self.id = id
		self.student_id = student_id
	def save():
		f = open('subjects.txt','w')
		id +=1
		f.write({},{}.format(self.name,self.id,self.student_id))
		f.close()
	def get_with_id(self,subject_id):
		files = open(subject_txt,'r')
		for line in files.readlines():
			datas = line.split(',')
			if int(datas[0]) == subject_id:
				self.id = subject_id
				self.name = datas[1]
				self.student_id = datas[2]
			return self
		return None

	def get_with_student_id(self,student_id):
		list_student = []
		files = open(student_txt, 'r')
		for line in files.readlines():
			datas = line.split(',')
			if int(datas[0]) == student_id:
				list_student.append(Subjects(id=int(datas[0]), name=datas[1]))
		files.close()
		return list_student
