def calculate_structure_sum(list_):
    sum_ = 0
    data = list(list_)
    while data:
        first = data[0]
        if isinstance(first, dict):
            for key, value in first.items():
                sum_ += len(key) + value
            data.pop(0)
        elif isinstance(first, list) or isinstance(first, tuple) or isinstance(first, set):
            sum_ += calculate_structure_sum(list(first))
            data.pop(0)
        elif isinstance(first, int) or isinstance(first, float):
            sum_ += first
            data.pop(0)
        elif isinstance(first, str):
            sum_ += len(first)
            data.pop(0)
    return sum_

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
