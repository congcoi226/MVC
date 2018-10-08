import os

room_txt = os.path.join(os.getcwd(), 'datas/rooms.txt')
id = 0


class Rooms(object):

    def __init__(self, id=0, name=None, address=None, seat=None):
        self.id = id
        self.name = name
        self.address = address
        self.seat = seat

    def save(self):
        f = open(room_txt,'a')
        self.id += 1
        f.write('\n{},{},{},{}'.format(self.id, self.name, self.address, self.seat))
        f.close()

    def get_with_id(self, room_id):
        files = open(room_txt, 'r')
        for line in files.readlines():
            datas = line.split(',')
            if int(datas[0]) == room_id:
                self.id = room_id
                self.name = datas[1]
                self.address = datas[2]
                self.seat = datas[3]
                return self
        return None
