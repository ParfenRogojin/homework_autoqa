import datetime

class Student():
    def __init__(self,name='',surname='',specialty='',start_year_studies=None,list_ratings=[]):
        self.name = name
        self.surname=surname
        self.specialty=specialty
        self.start_year_studies=start_year_studies
        self.list_ratings=list_ratings

    def add_score(self,score):
        self.list_ratings.append(score)

    def get_avg_rating(self):
        return sum(self.list_ratings)/len(self.list_ratings)

    def get_years_studies(self):
        return datetime.date.today().year-self.start_year_studies

    def __str__(self):
        return "Name = {0} {1}, specialty = {2}. start_year_studies = {3}".format(self.name, self.surname, self.specialty, self.start_year_studies)

if __name__ == '__main__':
    student1=Student('Ivan','Petrov','IT Engineer',2016,[5,4])
    print('\n__str:')
    print(student1)
    print("средний рейтинг: ",student1.get_avg_rating())
    student1.add_score(3)
    print("средний рейтинг: ",student1.get_avg_rating())
    print("сколько лет учится:  ",student1.get_years_studies())
