class SerialNumberObject:
    count = 0

    def __init__(self):
        SerialNumberObject.count += 1
        self.serial_num = SerialNumberObject.count

    def get_serial_num(self):
        return self.serial_num


def main():
    obj1 = SerialNumberObject()
    obj2 = SerialNumberObject()
    obj3 = SerialNumberObject()
    obj4 = SerialNumberObject()

    for i in (obj1, obj2, obj3, obj4):
        print(f'I am a object number {i.get_serial_num()}')


main()