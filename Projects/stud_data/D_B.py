import sqlite3
class TestData:


    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.cls = kwargs['cls']
        self.mark = kwargs['mark']
        self.grade = kwargs['grade']