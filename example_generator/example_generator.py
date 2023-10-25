import numpy as np


class AdditionGenerator():
    def __init__(self):
        self.configuration = {
            'number_range': [0, 30],
            'number_of_exercises': 10,
        }

    def generate_addition(self, result_in_range=False, result=False):
        number_range = self.configuration['number_range']

        for i in range(self.configuration['number_of_exercises']):
            if result_in_range:
                a = np.random.randint(number_range[0], number_range[1])
                b = np.random.randint(number_range[0], number_range[1] - a)
            
            else:
                a = np.random.randint(number_range[0], number_range[1])
                b = np.random.randint(number_range[0], number_range[1])


            if result:
                print(f'{a} + {b} = {a + b}')
            else:
                print(f'{a} + {b} =')