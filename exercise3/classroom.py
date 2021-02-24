# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:03:05 2021

@author: umera525
"""

class Person(object):
    def __init__(self, firstname, lastname):
        self._firstname = firstname
        self._lastname = lastname
    
    def name(self):
        return (self._firstname + ' ' + self._lastname)
    
class Student(Person):
    def __init__(self, firstname, lastname, subject):
        super(Student,self).__init__(firstname, lastname)
        self._subject = subject
    
    def printNameSubject(self):
        print(self.name(),', ', self._subject)

class Teacher(Person):
    def __init__(self, firstname, lastname, courses):
        super(Teacher,self).__init__(firstname, lastname)
        self._courses = courses
    
    def printNameCourses(self):
        print(self.name(),', ', self._courses)