
#Triple Quote is known as doc string
#__ system function
#__init__ system function to intialize
#__repr__ representation (when you look at it with the interactive prompt.)
#__str__ what happens when you print
#_ tells program that it should be private
# C.R.U.D. -> Create, Read, Update, Delete

GRADE_DICT = {
    "A" : 4.0,
    "B" : 3.0,
    "C" : 2.0,
    "D" : 1.0,
    "F" : 0.0
}

def convert_grade(letter_grade):
    if letter_grade in GRADE_DICT:
        return GRADE_DICT[letter_grade]
    else:
        return None


class Student:
    """
    Class to represent a unversity student. You must provide a banner ID to build a student class.
    """

    def __init__(self, banner_id):

        self.banner_id = banner_id
        self.name = ""
        self._grades = []
    
    def get_grades(self):
        return self._grades.copy

    def add_grade(self, grade):
        self._grades.append(grade.upper())

    def __repr__(self):
        return "{0} ({1}) \n{2}".format(self.name, self.banner_id, self._grades)

    def __str__(self):
        return "{0} ({1}) {2}".format(self.name, self.banner_id, self.get_gpa())

    def get_gpa(self):
        t = []
        for grade in self._grades:
            points = convert_grade(grade)
            if points is None:
                continue
            else:
                t.append(points)
        
        return sum(t) / len(t)
#End class student

s = Student(12345)
s.name = "Max Headroom"
s.add_grade("C")
s.add_grade("B")
s.add_grade("F")
s.add_grade("D")
s.add_grade("A")

print(s)