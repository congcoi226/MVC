from controllers.controllers import Controllers





def check_input_class_id(input):
    for i in range(2):
        class_id = check_input_class_id(input('Input your class id: '))
        if class_id:
            classes,subjects = Controllers().get_classes_and_subject_with_class_id(class_id)
        else:
            return False
        if subjects:
            for each_subject in subjects:
                print('Name Subject: ',each_subject.name)
        else:
            print('Not fine this class id')
        return True

def check_input_teacher_id(input):
    for i in range(2):
        teacher_id = check_input_teacher_id(input('Input your teacher id: '))
        if teacher_id:
            teachers,subjects = Controllers().get_teachers_and_subjects_with_teacher_id(teacher_id)
        else:
            return False
        if subjects:
            for each_subject in subjects:
                print('Name Subject: ',each_subject.name)
        else:
            print('Not fine this teacher id')
        return True

def check_input_subject_id(input):
    subject_id = check_input_subject_id(input('Input your subject id: '))
    if subject_id:
        students,subjects = Controllers().get_subject_and_student_with_subject_id(subject_id)
    else:
        return False
    if subjects:
        for each_subject in subjects:
            print('List Student: ',each_subject.name)
    else:
                print('Not fine this subject id')
    return True
