
from views.views import get_datas_school
from views.views import get_datas_class
from views.views import get_datas_room
from views.views import get_datas_subject
from views.views import get_datas_teacher
from views.views import get_datas_student
from views.views import get_subject_with_class_id
from views.views import get_subject_with_teacher_id
from views.views import get_student_with_subject_id



if __name__ == '__main__':
	get_datas_school()
	get_datas_class()
	get_datas_room()
	get_datas_subject()
	get_datas_teacher()
	get_datas_student()
	get_subject_with_class_id()
	get_subject_with_teacher_id()
	get_student_with_subject_id()
