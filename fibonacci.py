from typing import Union, List


class FibonacciMethod:
    epsilon: Union[int, float] = 0.01
    start_x: Union[int, float] = -3
    end_x: Union[int, float] = 7

    def example_function(self, x: Union[int, float]) -> Union[int, float]:
        """Функция-пример"""
        return x**2 + 2

    def get_fibonacci_numbers(self, end_number: Union[int, float]) -> List[int]:
        """Получение списка чисел фибоначчи, меньших заданного числа"""
        result: List[int] = [1, 1]
        while result[-1] < end_number:
            result.append(result[-1] + result[-2])
        return result

    def method(self) -> None:
        """Метод Фибоначчи поиска точки минимума функции"""
        f_numbers = self.get_fibonacci_numbers((self.end_x - self.start_x) / self.epsilon / 2)
        N = len(f_numbers) - 1

        current_start_x: Union[int, float] = self.start_x
        current_end_x: Union[int, float] = self.end_x
        different_start_and_end = current_end_x - current_start_x

        current_x1: Union[int, float] = current_start_x + f_numbers[N-2] * different_start_and_end / f_numbers[N]
        current_x2: Union[int, float] = current_start_x + f_numbers[N-1] * different_start_and_end / f_numbers[N]

        func_of_current_x1: Union[int, float] = self.example_function(current_x1)
        func_of_current_x2: Union[int, float] = self.example_function(current_x2)

        for counter in range(N - 3):
            if func_of_current_x1 <= func_of_current_x2:
                current_end_x = current_x2
                current_x2 = current_x1
                func_of_current_x2 = func_of_current_x1
                different_start_and_end = current_end_x - current_start_x
                current_x1 = current_start_x + f_numbers[N-counter-3] * different_start_and_end / f_numbers[N-counter-1]
                func_of_current_x1 = self.example_function(current_x1)
            else:
                current_start_x = current_x1
                current_x1 = current_x2
                func_of_current_x1 = func_of_current_x2
                different_start_and_end = current_end_x - current_start_x
                current_x2 = current_start_x + f_numbers[N-counter-2] / f_numbers[N-counter-1] + different_start_and_end
                func_of_current_x2 = self.example_function(current_x2)

        additional_x = current_x1 + self.epsilon
        func_of_additional_x = self.example_function(additional_x)
        if func_of_current_x1 <= func_of_additional_x:
            current_end_x = additional_x
        else:
            current_start_x = current_x1

        print(f'Начало отрезка, содержащего корень: {current_start_x}')
        print(f'Конец отрезка, содержащего корень: {current_end_x}')
        print(f'Приблизительный корень: {(current_start_x + current_end_x) / 2}')
        print(f'Количество шагов {N - 3}')
