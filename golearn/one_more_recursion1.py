# def encode(data):
#     if not data or len(data) < 2:
#         return data
#
#     for num, el in enumerate(data):
#         if data[0] != el:
#             return data[:1] + [num] + encode(data[num:])
#
#     return data[:1] + [len(data)]


# def encode(data):
#     if not data:
#         return []
#     curent_value = data[0]
#     count = 0
#     index_stop = 0
#     for index, value in enumerate(data):
#         if value != curent_value:
#             break
#         index_stop = index
#         count += 1
#     index_stop = index_stop + 1 if index_stop < len(data) else index_stop
#     return [curent_value, count] + encode(data[index_stop:])


def encode(data):
    if not data:
        return []
    index = 1
    while index < len(data) and data[index] == data[index - 1]:
        index = index + 1
    current = [data[0], index]
    return current + encode(data[index : len(data)])

print(encode(['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']))
