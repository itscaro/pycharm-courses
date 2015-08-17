import random

list1 = [9, 3, 63, 23, -12, 45, 9, -1, 23, 18, 73, 22, 109, -3, 5, 22]

list2 = []
for i in range(0, 15):
    list2.append(random.randrange(10000))

list3 = []
for i in range(0, 15):
    list3.append(round(random.uniform(-100.0, 100.0), 2))


def min(the_list):
    """
    Find and return the minimum in a list
    :param the_list: the input list
    :return: minimum
    """
Find the min number


def max(the_list):
    """
    Find and return the maximum in a list
    :param the_list: the input list
    :return: maximum
    """
Find the max number


min1 = min(list1)
max1 = max(list1)

min2 = min(list2)
max2 = max(list2)

min3 = min(list3)
max3 = max(list3)

message = "List %d : %s \n min is %f and max is %f"
print(Print the list, min and max numbers here)
print(Print the list, min and max numbers here)
print(Print the list, min and max numbers here)
