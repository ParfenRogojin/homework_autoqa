class Person():
    scope = ['people', 'something']

    def __init__(self, full_name='', year_of_birth=None):
        self.full_name = full_name
        assert (type(full_name) is str) and len(
            self.full_name.split(' ')) == 2, full_name + ' must contains Name[space]Surname'
        assert (type(year_of_birth) is int) and 1900 < year_of_birth < 2019, year_of_birth + ' wait int'
        self.year_of_birth = year_of_birth

    def get_name(self):
        return self.full_name.split(' ')[0]

    def get_surname(self):
        return self.full_name.split(' ')[1]

    def age_in(self, year=2018):
        return year - self.year_of_birth

    def __str__(self):
        return 'Name = '+self.get_name()+', Surname = '+self.get_surname()+', year_of_birth = '+str(self.year_of_birth)

if __name__ == '__main__':
    pn = Person('Vas Petrovich', 2000)
    print('Name:=' + pn.get_name())
    print('SurName:=' + pn.get_surname())
    print('Age in 2020:=', pn.age_in(2020))
    print('Age in 1990:=', pn.age_in(1990))
    print('year_of_birth:=', pn.year_of_birth)

    print(pn)
