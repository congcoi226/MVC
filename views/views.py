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

def get_datas_school():
	while True:
		schools = Controllers().get_datas_school()
		if schools:
			schools.save()
		play_again = input("Press 'n' to stop, other to continue: ")
		if play_again == 'n' or play_again == "N":
			break
def get_datas_class():
	while True:
		classes = Controllers().get_datas_class()
		if classes:
			classes.save()
		play_again = input("Press 'n' to stop, other to continue: ")
		if play_again == 'n' or play_again == "N":
			break
def get_datas_room():
	while True:
		rooms = Controllers().get_datas_room()
		if rooms:
			rooms.save()
		play_again = input("Press 'n' to stop, other to continue: ")
		if play_again == 'n' or play_again == "N":
			break
def get_datas_subject():
	while True:
		subjects = Controllers().get_datas_subject()
		if subjects:
			subjects.save()
		play_again = input("Press 'n' to stop, other to continue: ")
		if play_again == 'n' or play_again == "N":
			break
def get_datas_teacher():
	while True:
		teachers = Controllers().get_datas_teacher()
		if teachers:
			teachers.save()
		play_again = input("Press 'n' to stop, other to continue: ")
		if play_again == 'n' or play_again == "N":
			break
def get_datas_student():
	while True:
		students = Controllers().get_datas_student()
		if students:
			students.save()
		play_again = input("Press 'n' to stop, other to continue: ")
		if play_again == 'n' or play_again == "N":
			break



