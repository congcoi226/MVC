from controllers.controllers import Controllers





def get_subject_with_class_id():
    for i in range(2):
        try:
            class_id = int(input('Input your class id: '))
            classes,subjects = Controllers().get_classes_and_subject_with_class_id(class_id)
            if subjects:
                for each_subject in subjects:
                    print('Name Subject: ',each_subject.name)
            else:
                print('Not fine this class id')
            return True
        except (KeyError,ValueError):
            print('Your input is not integer. Please input again')
            continue
    print('You can not get teachers anymore')
    return False

def get_teacher_with_subject_id():
    for i in range(2):
        try:
            teacher_id = int(input('Input your teacher id: '))
            teachers,subjects = Controllers().get_teachers_and_subjects_with_teacher_id(teacher_id)
            if subjects:
                for each_subject in subjects:
                    print('Name Subject: ',each_subject.name)
            else:
                print('Not fine this teacher id')
            return True
        except (KeyError,ValueError):
            print('Your input is not integer. Please input again')
            continue
    print('You can not get teachers anymore')
    return False
def get_student_with_subject_id():
    for i in range(2):
        try:
            subject_id = int(input('Input your subject id: '))
            students,subjects = Controllers().get_subject_and_student_with_subject_id(subject_id)
            if subjects:
                for each_subject in subjects:
                    print('List Student: ',each_subject.name)
            else:
                print('Not fine this subject id')
            return True
        except (KeyError,ValueError):
            print('Your input is not integer. Please input again')
            continue
    print('You can not get teachers anymore')
    return False
