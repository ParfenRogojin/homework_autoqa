from homeWork.hw5_1_Person import Person


class Employee(Person):

    def __init__(self, name='', surname='', year_of_birth=None, position='', salary=0, experiens=0):
        assert (type(salary) in [float, int]) and salary >= 0, str(salary) + ' salary must be (float)>0.0'
        assert (type(experiens) in [float, int]) and experiens >= 0, str(
            experiens) + ' full_years_of_slavery must be (float)>0.0'
        Person.__init__(self, name + ' ' + surname, year_of_birth)
        self.salary = 1.0 * salary
        #        self.year_of_birth=year_of_birth
        self.position = position
        self.experience = experiens

    def get_position(self):
        mr1 = ['Junior', 'Middle', 'Senior']
        if self.experience > 6:
            return mr1[2] + ' ' + self.position
        return mr1[self.experience // 3] + ' ' + self.position

    def get_year_of_birth(self):
        return self.year_of_birth

    def income(self, months):
        return self.salary * months

    def add_salary(self, up=0):
        self.salary += up

    def __str__(self):
        return 'Name = {}, surname = {}, year of birth = {}, position = {} (expirens {}), salary = {}'.format(
            self.get_name(), self.get_surname(), self.year_of_birth, self.get_position(), self.experience, self.salary)


if __name__ == '__main__':
    pEmplArray = [Employee('Alex', 'Pushkin', 1901, 'Java Developer', 100.0, 0),
                  Employee('Nik', 'Lermontov', 2010, 'Pyton Developer', 200, 2),
                  Employee('Alex', 'Samsung', 1991, 'PM', 10.0, 3),
                  Employee('S20', 'Gnusmas', 1961, 'Engineer', 1200.0, 5),
                  Employee('R2D2', 'D2', 2002, 'PHP Software Engineer', 10.0, 6),
                  Employee('Scnd', 'LG', 1946, 'Data Analyst', 3100.0, 33)]

    for Empl in pEmplArray:
        print(Empl)
#        print('Name = {}, surname = {}, year of birth = {}, position = {} (expirens {}), salary = {}'.
#              format(Empl.get_name(), Empl.get_surname(), Empl.get_year_of_birth(), Empl.get_position(),
#                     Empl.experience, Empl.salary))

    print('\nSalary + 5000:')
    pEmplArray[5].add_salary(5000)
    Empl = pEmplArray[5]
    print('Name = {}, surname = {}, year of birth = {}, position = {} (expirens {}), salary = {}'.
          format(Empl.get_name(), Empl.get_surname(), Empl.get_year_of_birth(), Empl.get_position(), Empl.experience,
                 Empl.salary))
    print(Empl)
