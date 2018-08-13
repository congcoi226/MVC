import os

subject_txt = os.path.join(os.getcwd(), 'datas/subjects.txt')
student_txt = os.path.join(os.getcwd(), 'datas/students.txt')
id = 0
class Subjects(object):
	def __init__(self, name = None, id = 0):
		self.name = name
		self.id = id

	def save(self):
		f = open('subjects.txt','w')
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


def get_user_input():
	print("Please input data...")
	id = str(input('Subject ID: '))
	name = str(input('Name Subject: '))
	return Subjects(name,id)


if __name__ == '__main__':
	while True:
		subjects = get_user_input()
		if subjects:
			subjects.save()
		play_again = input("Press 'n' to stop, other to continue: ")
		if play_again == 'n' or play_again == 'N':
			break
