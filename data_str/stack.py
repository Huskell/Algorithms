

class stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, value):
        self.__stack_list.append(value)

    def pop(self):
        value = self.__stack_list[-1]
        del self.__stack_list[-1]
        return value
