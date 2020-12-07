def find_kth_largest(array, k)
  return nil if k > array.size

  find_kth_largest_recur(array, 0, array.size - 1, k)
end

def find_kth_largest_recur(array, low, high, k)
  return array[low] if low >= high

  r = partition(array, low, high)
  if k == r + 1
    array[r]
  elsif k < r + 1
    find_kth_largest_recur(array, 0, r - 1, k)
  else
    find_kth_largest_recur(array, r + 1, high, k)
  end
end

def partition(array, low, high)
  i = low
  j = low
  r = high
  pivot = array[r]
  while j < r
    if array[j] < pivot
      array[i], array[j] = array[j], array[i]
      i += 1
    end
    j += 1
  end
  array[i], array[r] = array[r], array[i]
  i
end

array = [4, 5, 6, 1, 2, 3]
puts(array.join(','))
item = find_kth_largest(array, 3)
puts(item)
