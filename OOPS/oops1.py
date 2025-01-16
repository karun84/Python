class course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def content(self):
        return f"Course code is: {self.course_code}, Course name is: {self.course_name}, Credit hours is: {self.credit_hours}"    

class coreCourse(course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major
        
    def content(self):
        info=super().content()
        if self.required_for_major:
            status="yes"
        else:
            status="no"
        return f"{info}, Whether required: {status}"

class electiveCourse(course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

core_Course=coreCourse("001","intro to cs", 3, False)
elective_Course=electiveCourse("002","example", 4, "general")

print(coreCourse.content())
print(electiveCourse.content())
