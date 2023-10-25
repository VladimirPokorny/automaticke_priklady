import numpy as np


class AdditionConfiguration():
    def __init__(self):
        self.number_range = [0, 30]
        self.result_in_range = True

class SubtractionConfiguration():
    def __init__(self):
        self.number_range = [0, 30]
        self.result_in_range = True


class ExampleConfiguration():
    def __init__(self):
        self.number_of_exercises_in_column = None
        self.number_of_columns = None
        self.show_results = None


class Generator():
    def __init__(self, example_configuration: ExampleConfiguration, 
                 addition_configuration: AdditionConfiguration, 
                 subtraction_configuration: SubtractionConfiguration,
                 parent=None):

        self.parent = parent
        self.example_configuration = example_configuration
        self.addition_configuration = addition_configuration
        self.subtraction_configuration = subtraction_configuration

    def generate_and_update_view(self):
        text = self.generate_addition_all()
        self.parent.text_edit.update_text(text)

    def generate_addition_all(self):      
        number_of_exercises_in_column = self.example_configuration.number_of_exercises_in_column
        number_of_columns = self.example_configuration.number_of_columns

        text = ''

        for row in range(number_of_exercises_in_column):
            for column in range(number_of_columns):
                text += self.generate_addition() + '\t'
            text += '\n'
        
        return text
      
    def generate_addition(self):
        number_range = self.addition_configuration.number_range
        result_in_range = self.addition_configuration.result_in_range
        show_results = self.example_configuration.show_results

        if result_in_range:
            a = np.random.randint(number_range[0], number_range[1])
            b = np.random.randint(number_range[0], number_range[1] - a)

        else:
            a = np.random.randint(number_range[0], number_range[1])
            b = np.random.randint(number_range[0], number_range[1])
        
        arguments = [a, b]
        np.random.shuffle(arguments)

        if show_results:
            return f'{arguments[0]} + {arguments[1]} = {sum(arguments)}'
        else:
            return f'{arguments[0]} + {arguments[1]} ='
        
    def generate_subtraction(self):
        number_range = self.subtraction_configuration
        result_in_range = self.subtraction_configuration.result_in_range
        show_results = self.example_configuration.show_results

        if result_in_range:
            a = np.random.randint(number_range[0], number_range[1])
            b = np.random.randint(number_range[0], number_range[1] - a)

        else:
            a = np.random.randint(number_range[0], number_range[1])
            b = np.random.randint(number_range[0], number_range[1])
        
        arguments = [a, b]
        np.random.shuffle(arguments)

        if show_results:
            return f'{arguments[0]} - {arguments[1]} = {sum(arguments)}'
        else:
            return f'{arguments[0]} - {arguments[1]} ='