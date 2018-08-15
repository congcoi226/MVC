
from views.views import get_subject_with_class_id
from views.views import get_subject_with_teacher_id
from views.views import get_student_with_subject_id
from views.views import input_school_data


if __name__ == '__main__':
	input_school_data()
	get_subject_with_class_id()
	get_subject_with_teacher_id()
	get_student_with_subject_id()
