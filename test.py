def count_group_begin_zero(n_customers: int) -> dict:
    """
    Функция подсчитывает число покупателей, попадающих в каждую группу.
    Группа = сумма всех цифр ID клиента.
    Нумерация ID сквозная и начинается с 0.
    На вход функция получает целое число  n_customers (количество клиентов)
    """

    dict_groups = {}
    for id in range(0, n_customers):
        group = 'group_' + str(sum(map(int, str(id))))
        if group in dict_groups:
            dict_groups[group] += 1
        else:
            dict_groups[group] = 0
            dict_groups[group] += 1


    return dict_groups



def count_group_begin_random(n_customers: int, n_first_id) -> dict:
    """
    Функция подсчитывает число покупателей, попадающих в каждую группу.
    Группа = сумма всех цифр ID клиента.
    ID начинается с произвольного числа
    На вход функция получает целое число  n_customers (количество клиентов) и n_first_id(первый ID последовательности)
    """

    dict_groups = {}
    for id in range(n_first_id, n_first_id + n_customers):
        group = 'group_' + str(sum(map(int, str(id))))
        if group in dict_groups:
            dict_groups[group] += 1
        else:
            dict_groups[group] = 0
            dict_groups[group] += 1


    return dict_groups