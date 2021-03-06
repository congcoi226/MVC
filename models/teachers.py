import os

teacher_txt = os.path.join(os.getcwd(), 'datas/teachers.txt')
subject_txt = os.path.join(os.getcwd(), 'datas/subjects.txt')

id = 0
class Teachers(object):

    def __init__(self,name = None,subject = None, id = 0, subject_id = 0):
        self.name = name
        self.subject = subject
        self.id = id
        self.subject_id = subject_id

    def save(self):
        f = open('teachers.txt','w')
        id +=1
        f.write({},{},{},{}.format(self.name, self.subject, self.id,self.subject_id))
        f.close()
    def get_with_id(self,teacher_id):
        files = open(teacher_txt,'r')
        for line in files.readlines():
            datas = line.split(',')
            if int(datas[0] == teacher_id):
                self.id = teacher_id
                self.name = datas[1]
                self.subject = datas[2]
                self.subject_id = datas[3]
            return self
        return None
    def get_with_subject_id(self, subject_id):
        list_subject = []
        files = open(subject_txt, 'r')
        for line in files.readlines():
            datas = line.split(',')
            if int(datas[0]) == subject_id:
                list_subject.append(Teachers(id=int(datas[0]), name=datas[1]))
        files.close()
        return list_subject