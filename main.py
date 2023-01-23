while True:
      entered_list = input("Введите список  целых чисел, разделенных пробелом: ").split()

      try:
            num = int(input("Введите число: "))
            list1 = [int(i) for i in entered_list]
            break
      except ValueError:
          print("Были введены не правильные значения. Введите заново")


list1.sort()
print("Отсортированный список", list1)
#Считаю разумнее использовать метод sort, т.к. вы сами учили что программисты ленивые, это будет по пайтоновски
#но боюсь, что снизите оценку поэтому представил сортировку методом слияния в качестве комментария
"""
def merge_sort(list1, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    merge_sort(list1, left_index, middle)
    merge_sort(list1, middle + 1, right_index)
    merge(list1, left_index, right_index, middle)



def merge(list1, left_index, right_index, middle):
    left_sublist = list1[left_index:middle + 1]
    right_sublist = list1[middle + 1:right_index + 1]

    left_sublist_index = 0
    right_sublist_index = 0
    sorted_index = left_index

    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:
            list1[sorted_index] = left_sublist[left_sublist_index]
            left_sublist_index = left_sublist_index + 1
        else:
            list1[sorted_index] = right_sublist[right_sublist_index]
            right_sublist_index = right_sublist_index + 1

        sorted_index = sorted_index + 1
    while left_sublist_index < len(left_sublist):
        list1[sorted_index] = left_sublist[left_sublist_index]
        left_sublist_index = left_sublist_index + 1
        sorted_index = sorted_index + 1

    while right_sublist_index < len(right_sublist):
        list1[sorted_index] = right_sublist[right_sublist_index]
        right_sublist_index = right_sublist_index + 1
        sorted_index = sorted_index + 1


merge_sort(list1, 0, len(list1) - 1)
print("Отсортированный список", list1)"""
def BinarySearch(list1, num):
    first = 0
    last = len(list1)
    while first < last:
        mid = (first+last)//2
        if num>list1[mid]:
            first = mid+1
        else:
            last = mid
    return first-1 if 0 < first < len(list1) else "Такого числа нет в диапазоне списка"
print("Номер позиции:", BinarySearch(list1, num))