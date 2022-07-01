def bubble_sort(a):
    """Sort input list using bubble sort algorithm"""

    # After each loop reduce the range by 1 to put the largest value of the checking range to the end of the range
    for i in range(len(a) - 1, 0, -1):
        # Compare each 2 adjacent numbers, move the largest value to the end of the checking range (i)
        for j in range(i):
            # If current value is larger than next value, swap them
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

        x = " ".join(list(map(str, a)))
        print(x)

    return x


def selection_sort(a):
    """Sort input list using selection sort algorithm"""

    # Put the smallest value to first index of the list
    for i in range(len(a)):
        # Assume current item is minimum, set a place-holder
        min_index = i
        # compare assumed minimum value to each value of the list
        for j in range(i + 1, len(a)):
            # if smaller value found, hold it index to place-holder (min_index)
            if a[j] < a[min_index]:
                min_index = j
        # After comparing with each item of the list, get the index of the smallest value and swap it with first assume
        a[i], a[min_index] = a[min_index], a[i]

        x = " ".join(list(map(str, a)))
        print(x)

    return x


def insertion_sort(a):
    """Sort input list using insertion sort algorithm"""

    # Compare current item (i) with previous items to find its place
    for i in range(1, len(a)):
        anchor = a[i]
        j = i - 1

        # Loop until no item behind is larger than current item
        while j >= 0 and a[j] > anchor:
            # Move previous item forward if it is larger than current item
            a[j + 1] = a[j]
            j -= 1
        # If previous item is smaller than current item, put current item in its place
        a[j + 1] = anchor

        x = " ".join(list(map(str, a)))
        print(x)

    return x


def merge_sort(lst):
    """Sort an input list using merge sort algorithm"""

    # Return item if recursive list has 1 or no item left
    if len(lst) <= 1:
        return lst

    # Divide list into smaller lists
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # Recursive call to sort each divided list
    left = merge_sort(left)
    right = merge_sort(right)

    # Return sorted merged list from 2 lists
    return merge(left, right)


def merge(l, r):
    """Return a sorted list from 2 input sorted lists"""

    res = []
    # Compare first item of 2 lists (the smallest item of each list)
    # append the smaller one to the final list and remove it from its list
    while len(l) != 0 and len(r) != 0:
        if l[0] < r[0]:
            res.append(l.pop(0))
        else:
            res.append(r.pop(0))

    # If either list is out of item, but the other still have items
    if len(l) == 0:
        res += r
    elif len(r) == 0:
        res += l

    return res

if __name__ == "__main__":
    lst = [10, 12, 2, 39, 18, 12, 1, 24, 13, 14, 12, 3]
    print("Sorted list:", sorted(lst))

    lst = [10, 12, 2, 39, 18, 12, 1, 24, 13, 14, 12, 3]
    bubble = bubble_sort(lst)
    print("Bubble:", bubble)

    lst = [10, 12, 2, 39, 18, 12, 1, 24, 13, 14, 12, 3]
    selection = selection_sort(lst)
    print("Selection:", selection)

    lst = [10, 12, 2, 39, 18, 12, 1, 24, 13, 14, 12, 3]
    insertion = insertion_sort(lst)
    print("Insertion:", insertion)

    lst = [10, 12, 2, 39, 18, 12, 1, 24, 13, 14, 12, 3]
    merged = merge_sort(lst)
    print("Merge:", merged)