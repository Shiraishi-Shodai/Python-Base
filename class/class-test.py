import math


class SchoolReport:
    
    # クラス変数(オブジェクトで共通した変数)
    school_name = 'さぷー中学校'
    
    # コンストラクタ
    def __init__(self, student_name, math_score, jp_score, en_score):
        self.student_name = student_name
        self.math_score = math_score
        self.jp_score = jp_score
        self.en_score = en_score
        
    def calc_avg_score(self):
        avg_score = (self.math_score + self.jp_score + self.en_score) / 3
        return f'平均点は{math.floor(avg_score)}点です'

sr = SchoolReport('田中A', 100, 80, 30)
# print(sr.student_name)

print(sr.calc_avg_score())
print(SchoolReport.school_name) #インスタンス化しなくてもアクセスできる
print(sr.school_name)

SchoolReport.school_name = 'サプー中学校'
print(SchoolReport.school_name) 
print(sr.school_name)