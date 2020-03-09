import unittest
from homeWork.hw5_1_ITEmployee import ITEmployee


class task5_4(unittest.TestCase):

    def test_ITEml_01_skills(self):
        rezult = ITEmployee('Alex', 'Pushkin', 1901, 'Java Developer', 100.0, 0, skills=['DewOps', 'Admin']).skills
        self.assertEqual(rezult, ['DewOps', 'Admin'])

    def test_ITEml_02_addSkill(self):
        itEmp = ITEmployee('Alex', 'Pushkin', 1901, 'Java Developer', 100.0, 0, skills=['DewOps', 'Admin'])
        itEmp.add_skill(['Dance', ])
        rezult = itEmp.skills
        self.assertEqual(rezult, ['DewOps', 'Admin', 'Dance'])

    def test_ITEml_03_salary(self):
        itEmp = ITEmployee('Alex', 'Pushkin', 1901, 'Java Developer', 100.0, 0, skills=['DewOps', 'Admin'])
        itEmp.add_salary(1000)
        rezult = itEmp.salary
        self.assertEqual(rezult, 1100.0)

    def test_ITEml_04_income(self):
        itEmp = ITEmployee('Alex', 'Pushkin', 1901, 'Java Developer', 100.0, 0, skills=['DewOps', 'Admin'])
        itEmp.add_salary(1000)
        rezult = itEmp.income(10)
        self.assertEqual(rezult, 11000.0)

    def test_ITEml_05_get_year_of_birth(self):
        rezult = ITEmployee('Alex', 'Pushkin', 1901, 'Java Developer', 100.0, 0,
                            skills=['DewOps', 'Admin']).year_of_birth
        self.assertEqual(rezult, 1901)

    def test_ITEml_06_expirence_position(self):
        rezult = ITEmployee('Alex', 'Pushkin', 1901, 'Java Developer', 100.0, 6,
                            skills=['DewOps', 'Admin']).get_position()
        self.assertEqual(rezult, 'Senior Java Developer')


if __name__ == '__main__':
    unittest.main()
