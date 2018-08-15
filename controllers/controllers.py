from models.classes import Classes
from models.rooms import Rooms
from models.schools import Schools
from models.students import Students
from models.teachers import Teachers
from models.subjects import Subjects


class Controllers(object):

    def get_schools(self, school_id):
        response_school = Schools().get_with_id(school_id)
        if not response_school:
            return None, None

    def get_teachers_and_subjects_with_teacher_id(self, teacher_id):
        response_teacher = Teachers().get_with_id(teacher_id)
        if not response_teacher:
            return None, None
        response_subject = Teachers().get_with_subject_id(teacher_id)
        return response_teacher, response_subject

    def get_subject_and_student_with_subject_id(self, subject_id):
        response_subject = Subjects().get_with_id(subject_id)
        if not response_subject:
            return None, None
        response_student = Subjects().get_with_student_id(subject_id)
        return response_subject, response_student

    def get_teachers(self, teacher_id):
        response_teacher = Teachers().get_with_id(teacher_id)
        if not response_teacher:
            return None, None

    def get_class_and_room_with_room_id(self, room_id):
        response_room = Rooms().get_with_id(room_id)
        if not response_room:
            return None, None
        response_classes = Classes().get_with_room_id(room_id)
        return response_room, response_classes


    def get_classes_and_subject_with_class_id(self,class_id):
        response_subject = Classes().get_with_id(class_id)
        if not response_subject:
            return None, None
        response_classes = Classes().get_with_subject_id(class_id)
        return response_subject, response_classes

    def create_school(self, name, address):
        if len(name) < 3:
            return False
        school = Schools(name, address)
        school.save()
        return True