from homeWork.hw4_t1_3 import clrNonAlph

class Container_Generators:
    def __init__(self):
        pass

    def generator_1_2N(self, n=20):
        # 1) Создайте список 2 в степени N, где N от 0 до 20.
        # rezult_list = []
        # for i in range(n + 1):
        #     rezult_list.append(2 ** i)
        # return rezult_list
        return [2 ** i for i in range(n+1)]

    def generator_2_div3(self, n=20):
        # 2) У вас есть список целых чисел. Создайте новый список остатков от деления на 3 чисел из исходного списка
        # rezult_list = []
        # for i in range(n + 1):
        #     rezult_list.append(i // 3)
        # return rezult_list
        return [i//3 for i in range(n+1)]

    def generator_3_num(self, get_list):
        # # 3)вас есть список, в котором могут быть разные типы данных. Создайте новый список только чисел из этого списка
        # rez_list = []
        # for item in get_list:
        #     if type(item) in [int, float]:
        #         rez_list.append(item)
        # return rez_list
        return [item for item in get_list if type(item) in [int, float]]

    def generator_4_alph(self, get_list):
        # 4) есть список, в котором могут быть разные типы данных. Создайте новый список только строк, при этом удалите усе небуквенные символы из них. Воспользуйтесь функцией из предыдущего задания (импортируйте её из другого своего файла
        # rez_list = []
        # for item in get_list:
        #     rez_list.append(clrNonAlph(item))
        # return rez_list
        return [clrNonAlph(item) for item in get_list]

    def generator_5_type_in_item(self, get_dict):
        # rez_dict = {}
        # for item in get_dict:
        #     rez_dict[item] = type(get_dict.get(item))
        # return rez_dict
        return {k:str(type(v))[8:-2:] for k,v in get_dict.items()}

    def generator_5_str_in_item(self, get_dict):
        # rez_dict = {}
        # for item in get_dict:
        #     if type(get_dict.get(item)) == str:
        #         rez_dict[item] = clrNonAlph(get_dict.get(item)).lower()
        # return rez_dict
        return {k:(clrNonAlph(item).lower()) for k,item in get_dict.items() if type(item) == str}

if __name__ == '__main__':
    cont = Container_Generators()

    print('# 1) Создайте список 2 в степени N, где N от 0 до 20.')
    print(cont.generator_1_2N())

    print(
        '\n# 2) У вас есть список целых чисел. Создайте новый список остатков от деления на 3 чисел из исходного списка')
    print(cont.generator_2_div3())

    print(
        '\n# 3) вас есть список, в котором могут быть разные типы данных. Создайте новый список только чисел из этого списка')
    src = ['weff)333_', 123, [12, 34], '**', 4.5, '43542', 'SGAS', 'Adiu', 'Syt']
    print(src)
    print(cont.generator_3_num(src))

    print(
        '\n# 4) есть список, в котором могут быть разные типы данных. Создайте новый список только строк, \nпри этом удалите усе небуквенные символы из них. Воспользуйтесь функцией из предыдущего задания (импортируйте её из другого своего файла')
    src = ['weff)333_dsf', 'vcb332', '*df', '**', 'dsg', '43542', 'SGAS', 'ADSfd', 'Adiu', 'Syt']
    print(src)
    print(cont.generator_4_alph(src))

    print(
        '\n# 5) У вас есть словарь – характеристик человека. Ключи например: “name”, “surname”, “age”, “position”, “address”, “skills”.')

    srcDic = {'name': 'Leonid', 'surname': 'First', 'age': 1600, 'position': 'King', 'address': 'Sparta',
              'Skills': ['God', ]}
    print('## Сгенерируйте новый словарь с такими же ключами, а в значениях типы значений.')
    print(srcDic)
    print(cont.generator_5_type_in_item(srcDic))
    print(
        '\n## Сгенерируйте новый словарь с только парами ключ-значение, если значение исходного словаря было строкой. \nЗначения нового словаря должны быть переведены в нижний регистр и удалены небуквенные символы из них')
    srcDic = {'name': 'Leonid777', 'surname': 'First', 'age': 1600, 'position999': 'King', 'address': 'Sparta',
              'Skills': ['God', ]}
    print(srcDic)

    print(cont.generator_5_str_in_item(srcDic))
