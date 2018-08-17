
from views.views import get_subject_with_class_id
from views.views import get_subject_with_teacher_id
from views.views import get_student_with_subject_id
from views.views import input_school_datas
from views.views import input_class_datas
from views.views import input_room_datas
from views.views import input_subject_datas
from views.views import input_teacher_datas
from views.views import input_student_datas




if __name__ == '__main__':
	input_school_datas()
	input_class_datas()
	input_room_datas()
	input_subject_datas()
	input_teacher_datas()
	input_student_datas()
	get_subject_with_class_id()
	get_subject_with_teacher_id()
	get_student_with_subject_id()
