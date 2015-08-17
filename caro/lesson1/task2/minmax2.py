import random

list1 = [9, 3, 63, 23, -12, 45, 9, -1, 23, 18, 73, 22, 109, -3, 5, 22]

list2 = []
for i in range(0, 15):
    list2.append(random.randrange(10000))

list3 = []
for i in range(0, 15):
    list3.append(round(random.uniform(-100.0, 100.0), 2))


def minAndMax(the_list):
    """
    Find and return the minimum and maximum of a list
    :param the_list: the input list
    :return:
    """
Use one function only

Using minAndMax() to find min and max numbers of these lists

message = "List %d : %s \n min is %f and max is %f"
print(message % (1, list1, min1, max1))
print(message % (2, list2, min2, max3))
print(message % (3, list3, min3, max2))
