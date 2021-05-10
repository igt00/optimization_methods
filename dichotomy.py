from typing import Union


class DichotomyMethod:
    epsilon: Union[int, float] = 0.01
    start_x: Union[int, float] = -3
    end_x: Union[int, float] = 7
    step_for_x: Union[int, float] = 0.02

    def example_function(self, x: Union[int, float]) -> Union[int, float]:
        """Функция-пример"""
        return x**2 + 2

    def method(self) -> None:
        """Метод дихотомии поиска точки минимума функции"""
        current_start_x: Union[int, float] = self.start_x
        current_end_x: Union[int, float] = self.end_x
        different_between_start_and_end: Union[int, float] = current_end_x - current_start_x
        counter: int = 0

        while different_between_start_and_end > 2 * self.epsilon:
            current_x1: Union[int, float] = (current_start_x + current_end_x - self.step_for_x) / 2
            current_x2: Union[int, float] = (current_start_x + current_end_x + self.step_for_x) / 2
            func_of_current_x1: Union[int, float] = self.example_function(current_x1)
            func_of_current_x2: Union[int, float] = self.example_function(current_x2)

            if func_of_current_x1 < func_of_current_x2:
                current_end_x = current_x2
            elif func_of_current_x1 > func_of_current_x2:
                current_start_x = current_x1
            else:
                current_start_x = current_x1
                current_end_x = current_x2

            different_between_start_and_end = current_end_x - current_start_x
            counter += 1

        print(f'Начало отрезка, содержащего корень: {current_start_x}')
        print(f'Конец отрезка, содержащего корень: {current_end_x}')
        print(f'Приблизительный корень: {(current_start_x + current_end_x) / 2}')
        print(f'Количество шагов {counter}')
