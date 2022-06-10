class Student:
    curr_class = None
    class_list = []

    def __init__(self, name):
        self.name = name
        #MyClass.count += 1

    def addClass(self, class_name):
        self.class_list.append(class_name)
        print(f'Student.class_list id :: {id(Student.class_list)}')
        print(f'self.class_list id :: {id(self.class_list)}')

    def currClass(self, class_name):
        self.curr_class = class_name
        print(f'Student.curr_class :: {Student.curr_class}')
        print(f'Student.curr_class id :: {id(Student.curr_class)}')
        print(f'self.curr_class :: {self.curr_class}')
        print(f'self.curr_class id :: {id(self.curr_class)}')

def main():
    student1 = Student('hyunsuki')
    student1.addClass('Korean')
    student1.currClass('Korean')
#    student1.addClass('English')
#    print(Student.class_list)
#    student2 = Student('shb')
#    student2.addClass('Korean')
#    print(f"student1's class_list :: {student1.class_list}")
#    print(f"student1's class_num :: {student1.class_num}")
#    print(f"student2's class_list :: {student2.class_list}")
#    print(f"student2's class_num :: {student2.class_num}")


if __name__ == '__main__':
    main()
