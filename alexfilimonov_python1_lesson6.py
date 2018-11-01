class People:
    def __init__(self, name, middlename, surname, birth_date, school):
        self.name = name
        self.middlename = middlename
        self.surname = surname
        self.birth_date = birth_date
        self.school = school		

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name

    def print_parents_fio(self):
        return ' Student:' + self.name + ' ' + self.middlename + ' ' + self.surname + ', Mother:' + self.mother_fio + ', Father:' + self.father_fio

# Класс Student наследуется от класса People ------------------------------------------------------------------
class Student(People):
    def __init__(self, name, middlename, surname, birth_date, school, class_room, mother_fio, father_fio):
        self.name = name
        self.middlename = middlename
        self.surname = surname
        self.birth_date = birth_date
        self.school = school

        # Добавляем уникальные атрибуты
        self.mother_fio = mother_fio
        self.father_fio = father_fio
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}

    # И уникальные методы
    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

    def next_class(self):
        self._class_room['class_num'] += 1

# Класс Teacher наследуется от класса People ------------------------------------------------------------------
class Teacher(People):
    def __init__(self, name, middlename, surname, birth_date, school, teach_class):
		# Явно вызываем конструктор родительского класса
        People.__init__(self, name, middlename, surname, birth_date, school)
		# Добавляем уникальные атрибуты
        self._class_room = {'class_num': int(teach_class.split()[0]),
                            'class_char': teach_class.split()[1]}
        self._class_room_subject = {'class_num': int(teach_class.split()[0]),
                            'class_char': teach_class.split()[1], 
                            'class_subject': teach_class.split()[2]}	
        #self.teach_classes = list(map(self.convert_class, teach_classes))

    # Уникальный метод Учителя - какой предмет в каком классе преподает:
    @property
    def class_room(self):
        return "{} {}".format(self._teach_class['class_num'], self._teach_class['class_char'])
    @property
    def class_room_subject(self):
        return "{} {} {}".format(self._teach_class['class_num'], self._teach_class['class_char'], self._teach_class['class_subject'])
	
    def convert_class(self, class_room_subject):
        """
        '<class_num> <class_int>' --> {'class_num': <class_num>, 'class_int': <class_int>}
        """
        return {'class_num': int(class_room_subject.split()[0]),
                'class_char': class_room_subject.split()[1], 
                'class_subject': class_room_subject.split()[2]}				

# Класс Subject (предмет) --- NOT USED HERE, FOR FUTURE!
class Subject:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.subject_classes = list(map(self.convert_class, subject_classes))

    def get_subject_name(self):
        return self.name 

    def set_subject_name(self, new_name):
        self.name = new_name

    # Уникальный метод 
    def convert_class(self, class_room):
        """
        '<class_num> <class_int>' --> {'class_num': <class_num>, 'class_int': <class_int>}
        """
        return {'class_num': int(class_room.split()[0]),
                'class_char': class_room.split()[1]}

# Инициализируем студентов: ---------------------------------------------------------
students =[
    Student("Ivan", "Petrovich", "Ivanov", '10.11.2000', "school №5", "10 A","Ivanova Anna Sergeevna","Ivanov Petr Yurievich"),
    Student("Zanna", "Petrovna", "Yuzina", '11.12.2000', "school №5", "10 A","Yuzina Maina Ivanovna","Yuzin Petr Igorevich"),    
    Student("Pavel", "Andreevich", "Rezkiy", '1.2.2001', "school №5", "9 A","Rezkaya Anna Andreevna","Rezkiy Andrey Valentinovich"),
    Student("Anna", "Andreevna", "Kysh", '20.11.2001', "school №5", "9 B","Ivanova Marina Sergeevna","Kysh Andrey Yurevich"),
    ]
# Инициализируем учителей: ---------------------------------------------------------
teachers =[
    Teacher("Ivan", "Petrovich", "Serafimov", '10.11.1980', "school №5", "10 A Mathematics"),
    Teacher("Ivan", "Petrovich", "Serafimov", '10.11.1980', "school №5", "9 A Mathematics"),	
    Teacher("Zanna", "Petrovna", "Yuzina", '11.12.1970', "school №5", "10 A English"),    
    Teacher("Pavel", "Andreevich", "Belkin", '1.2.1971', "school №5", "9 A English"),
    Teacher("Anna", "Andreevna", "Agafonova", '20.11.1972', "school №5", "9 B Physics"),
    ]
	
	
# Задание №1: Получить полный список всех классов школы---------------------------------------------------------------	
full_classes_list = []
for student in students:
    if (student._class_room not in full_classes_list) : 
	    full_classes_list.append(student._class_room)
print('')
print('Task #1: All classes list in school #5:')		
print(full_classes_list)
	
# Задание №2: Получить полный список учеников в указанном классе школы-----------------------------------------------
print('')
print('Task #2: All student list in classes of the school #5:')		
for classes in full_classes_list:
    full_class_student_list = []
    for student in students:
        if (student._class_room == classes) : 
	        full_class_student_list.append(student.name+' '+student.middlename+' '+student.surname)			
    print("")			
    print(classes)
    print(full_class_student_list)

# Задание №3: Получить список всех предметов каждого ученика----------------------------------------------------------------------	
print('')
print('Task #3: All subjects list in class for each student of the school #5:')		
for student in students: 
    for teacher in teachers:    
        if (student._class_room == teacher._class_room)	:
            print('Student: '+student.name+' '+student.middlename+' '+student.surname) 
            print(teacher._class_room_subject)  			

	
# Задание №4: Напечатать ФИО родителей учеников----------------------------------------------------------------------	
print('')
print('Task #4: All parents names of all students:')	
for student in students:
    print(student.print_parents_fio())
	
# Задание №5: Получить список всех учителей в указанном классе----------------------------------------------------------------------	
print('')
print('Task #5: All teachers list for each class of the school #5:')		
for classes in full_classes_list:
    print(classes) 
    for teacher in teachers:    
        if (classes == teacher._class_room)	:
            print('Teacher: '+teacher.name+' '+teacher.middlename+' '+teacher.surname) 

	


	