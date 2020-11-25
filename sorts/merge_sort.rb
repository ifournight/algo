# frozen_string_literal: true

def merge_sort(array)
  merge_sort_recur(array, 0, array.size - 1)
end

def merge_sort_recur(array, low, high)
  return if low >= high

  mid = low + (high - low) / 2
  merge_sort_recur(array, low, mid)
  merge_sort_recur(array, mid + 1, high)
  merge(array, low, mid, high)
end

def merge(array, low, mid, high)
  i = low # low pointer
  j = mid + 1 # high pointer
  merged = []
  while (i <= mid) && (j <= high)
    if array[i] < array[j]
      merged << array[i]
      i += 1
    else
      merged << array[j]
      j += 1
    end
  end
  merged += i <= mid ? array[i..mid] : array[j..high]
  array[low..high] = merged
end

array = []
10.times { array << rand(20) }
puts(array.join(','))
merge_sort(array)
puts(array.join(','))
