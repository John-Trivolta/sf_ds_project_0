"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict():
    """Рандомно угадываем число

    
    Returns:
        int: Число попыток
    """
    
    predict_number = np.random.randint(1, 101)  # загаданное компьютером число
    
    min=1 
    max=100 
    
    count = 0

    while True:
        count += 1
        num = (min + max)//2
        if num < predict_number:
            min = num + 1
        elif num > predict_number:
            max = num - 1
        else:                
            break  # выход из цикла если число угадано
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
 
    for i in range(1000):
        count_ls.append(random_predict())  
       

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    
