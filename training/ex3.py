from student import Student
from course_group import CourseGroup


student = Student("Кристина", "Калабурдина", 36, "Инженер по тестированию")
classmate1 = Student("Владимир", "Валько", 35, "Инженер по тестированию")
classmate2 = Student("Виктория", "Бурлаченко", 28, "Инженер по тестированию")
classmate3 = Student("Василий", "Пупкин", 26, "Инженер по тестированию")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])

print(course_group)
