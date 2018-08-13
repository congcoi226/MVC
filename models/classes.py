import os

class_txt = os.path.join(os.getcwd(), 'datas/classes.txt')
subject_txt = os.path.join(os.getcwd(), 'datas/subjects.txt')
id = 0


class Classes(object):

    def __init__(self, id=0, name=None, address=None, subject_id=None):
        self.id = id
        self.name = name
        self.address = address
        self.subject_id = subject_id

    def save(self):
        f = open('classes.txt','w')
        f.write('{},{},{},{},'.format(id, self.name, self.address, self.subject_id))
        f.close()

    def get_with_id(self, class_id):
        files = open(class_txt, 'r')
        for line in files.readlines():
            datas = line.split(',')
            if int(datas[0]) == class_id:
                self.id = class_id
                self.name = datas[1]
                self.address = datas[2]
                return self
        return None

    def get_with_subject_id(self, subject_id):
        list_subject = []
        files = open(subject_txt, 'r')
        for line in files.readlines():
            datas = line.split(',')
            if int(datas[0]) == subject_id:
                list_subject.append(Classes(id=int(datas[0]), name=datas[1]))
        files.close()
        return list_subject


def get_user_input():
    print("Please input data...")
    id = str(input('Class ID: '))
    name = str(input('Name Class: '))
    address = str(input('Address: '))
    return Classes(name, address, id)

if __name__ == '__main__':
    while True:
        classes = get_user_input()
        if classes:
            classes.save()
        play_again = input("Press 'n' to stop, other to continue: ")
        if play_again == 'n' or play_again == "N":
            break