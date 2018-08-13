import os

student_txt = os.path.join(os.getcwd(), 'datas/students.txt')

id = 0

class Students(object):

    def __init__(self,name = None,address = None,id = 0):
        self.name = name
        self.address = address
        self.id = id

    def save(self):
        f = open('students.txt','w')
        f.close()
    def get_with_id(self, student_id):
        files =  open(student_txt,'r')
        for line in files.readlines():
            datas = lines.split(',')
            if int(data[0]) == student_id:
                self.id = student_id
                self.name = data[1]
                self.address = data[2]
            return self
        return None


def get_user_input():
    print("Please input data...")
    id = str(input('ID Student: '))
    name = str(input('Name Student: '))
    if len(name) <=3:
        print('Name must have more than 3 characters')
        return None
    address = str(input('Address: '))
    return Students(name, address, id)

if __name__ == '__main__':
    while True:
        student = get_user_input()
        if student:
            student.save()
        play_again = input("Press 'n' to stop, other to continue: ")
        if play_again == 'n' or play_again == "N":
            break      

