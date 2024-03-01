# values = (0, 1, 2)

# if any(values):

#   my_var = 0

# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

# if  all(my_list[:6]) or all(my_list[:]):

#   print("Good")

# else:

#   print("Bad")
# v = 40

# my_range = list(range(v))

# print(sum(my_range, v) + pow(v, v, v))  # 820
# print((80**40)%40)
# l=list(range(20))
# print(sum(l)/20)
# my_all
# print(my_all([1, 2, 3])) # True
# print(my_all([1, 2, 3, []])) # False

# # my_any
# print(my_any([0, 1, [], False])) # True
# print(my_any([(), 0, False])) # False

# # my_min
# print(my_min([10, 100, -20, -100, 50])) # -100
# print(my_min((10, 100, -20, -100, 50))) # -100

# # my_max
# print(my_max([10, 100, -20, -100, 50, 700])) # 700
# print(my_max((10, 100, -20, -100, 50, 700))) # 700
def my_min(*numbers):
    if not numbers:
        return None

    min_number = numbers[0]

    for number in numbers:
        if number < min_number:
            min_number = number

    return min_number

# قائمة الأرقام للاختبار
numbers_list = [10, 5, 8, 20, 3, 15, 7]

# الحصول على الرقم الأكبر
print(my_min(10, 100, -20, -100, 50))

# طباعة النتيجة


