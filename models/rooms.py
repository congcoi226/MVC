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
        f = open('room.txt','w')
        f.write('{},{},{},{},'.format(id, self.name, self.address, self.seat))
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


def get_user_input():
    print("Please input data...")
    id = str(input('Room ID: '))
    name = str(input('Name Room: '))
    address = str(input('Address: '))
    return Rooms(name, address, id)

if __name__ == '__main__':
    while True:
        room = get_user_input()
        if room:
            room.save()
        play_again = input("Press 'n' to stop, other to continue: ")
        if play_again == 'n' or play_again == "N":
            break