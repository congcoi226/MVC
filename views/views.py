from controllers.controllers import Controllers


def get_input():
	for i in range(2):
		try:
			input_id = int(input('Please input id: '))
			return input_id
		except (KeyError,ValueError):
			continue
	return False


def get_subject_with_class_id():
	print('Get subject with class id')
	class_id = get_input()
	if class_id:
		classes,subjects = Controllers().get_classes_and_subject_with_class_id(class_id)
	else:
		return False
	if subjects:
		for each_subject in subjects:
			print('Name Subject: ',each_subject.name)
	else:
		print('Not find this class id')
	return True

def get_subject_with_teacher_id():
	print('Get subject with teacher id')
	teacher_id = get_input()
	if teacher_id:
		teachers,subjects = Controllers().get_teachers_and_subjects_with_teacher_id(teacher_id)
	else:
		return False
	if subjects:
		for each_subject in subjects:
			print('Name Subject: ',each_subject.name)
	else:
		print('Not find this teacher id')
	return True

def get_student_with_subject_id():
	print('Get student with subject id')
	subject_id = get_input()
	if subject_id:
		students,subjects = Controllers().get_subject_and_student_with_subject_id(subject_id)
	else:
		return False
	if subjects:
		for each_subject in subjects:
			print('List Student: ',each_subject.name)
	else:
		print('Not find this subject id')
	return True

def input_school_datas():
	print('Please enter school data...')
	name = input('School name (more than 3 chars) : ')
	address = input('Address: ')
	result = Controllers().create_school(name, address)
	if result:
		print('A new school is created sucessfully.')
	else:
		print('Failed to create a new school.')

def input_class_datas():
	print('Please enter class data...')
	name = input('Class name: ')
	address = input('Address: ')
	result = Controllers().creat_class(name , address)
	if result:
		print('A new class is created sucessfully.')
	else:
		print('Failed to creat a new class.')

def input_room_datas():
	print('Please enter room data...')
	name = input('Room name: ')
	address = input('Address: ')
	seat = input('Seats: ')
	result = Controllers().creat_room(name , address, seat)
	if result:
		print('A new room is created sucessfully.')
	else:
		print('Failed to creat a new room.')

def input_subject_datas():
	print('Please enter subject data...')
	name = input('Subject name: ')
	result = Controllers().creat_subject(name)
	if result:
		print('A new subject is created sucessfully.')
	else:
		print('Failed to creat a new subject.')

def input_teacher_datas():
	print('Please enter teacher data...')
	name = input('Teacher name: ')
	subject = input('Subject: ')
	result = Controllers().creat_teacher(name,subject)
	if result:
		print('A new teacher is created sucessfully.')
	else:
		print('Failed to creat a new teacher.')

def input_student_datas():
	print('Please enter student data...')
	name = input('Student name: ')
	address = input('Address: ')
	result = Controllers().creat_student(name,address)
	if result:
		print('A new student is created sucessfully.')
	else:
		print('Failed to creat a new student.')


