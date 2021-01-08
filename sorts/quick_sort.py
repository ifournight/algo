# coding: UTF-8

def quick_sort(a):
  quick_sort_r(a, 0, len(a) - 1)
  
def quick_sort_r(a, low, high):
    if low >= high:
        return
    m = partition(a, low, high)
    quick_sort_r(a, low, m - 1)
    quick_sort_r(a, m + 1, high)

def partition(a, low, high):
    r = high
    pivot = a[r]
    i = low
    for j in range(low, high):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i

if __name__ == '__main__':
    a = [(5, 1), (5, 2), (5, 3), (3, 1), (2, 1), (1, 1)]
    quick_sort(a)
    print(a)