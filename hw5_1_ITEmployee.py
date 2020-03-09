from homeWork.hw5_1_Employee import Employee

class ITEmployee(Employee):
    def __init__(self,*param,skills=[]):
        Employee.__init__(self,*param)
        self.skills=skills

    def add_skill(self,new_skills):
        self.skills.extend(new_skills)
            #append(new_skills)
    def __str__(self):
        return Employee.__str__(self)+'// Skills: '+str(self.skills)

if __name__ == '__main__':
    ITEmpl = ITEmployee('Alex', 'Pushkin', 1901, 'Java Developer', 100.0, 0, skills=['DewOps', 'Admin'])
    print(ITEmpl.skills)
    ITEmpl.add_skill(['Singer','Waiter'])
    print(ITEmpl.skills)
    print(ITEmpl)