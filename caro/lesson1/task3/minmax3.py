import random

list_sub_1 = []
for i in range(0, 15):
    list_sub_1.append(random.randrange(10000))

list_sub_2 = []
for i in range(0, 15):
    list_sub_2.append(round(random.uniform(-100.0, 100.0), 2))

list1 = [9, 3, 63, 23, -12, 45, 9, -1, 23, 18, 73, 22, 109, -3, 5, 22, list_sub_1, list_sub_2]


def minAndMax(the_list):
    """
    Find and return the minimum and maximum of a list
    :param list: the input list
    :return:
    """
Find the smallest and largest numbers in the list


[min1, max1] = minAndMax(list1)

message = "List %d : %s \n min is %f and max is %f"
print(message % (1, list1, min1, max1))
