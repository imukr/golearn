# def all_sub_lists(data):
#     new_list = []
#     for n in range(len(data)):
#         for j in range(len(data)+1):
#           print(n,j)
#           new_list.append(data[n:j+n])
#     print(new_list)
# all_sub_lists([4, 6, 1, 3])

def all_sub_lists(data):
    sublists = [[]]
    for length in range(1, len(data) + 1):
        print(length)
        for i in range(len(data) - length + 1):
            sublists.append(data[i: i + length])
            print(i,i+length)
    return print(sublists)
all_sub_lists([4, 6, 1, 3])

