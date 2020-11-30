def heap_sort(array)
  build_max_heap(array)
  i = array.size - 1
  while i.positive?
    array[i], array[0] = array[0], array[i]
    i -= 1
    max_heapify(array, 0, i)
  end
end

def build_max_heap(array)
  last_parent_index = ((array.size - 1) - 1) / 2
  i = last_parent_index
  while i >= 0
    max_heapify(array, i, array.size - 1)
    i -= 1
  end
end

def max_heapify(array, start_index, end_index)
  current_index = start_index
  left_index = current_index * 2 + 1
  right_index = current_index * 2 + 2
  max_index = current_index
  if left_index <= end_index && array[left_index] > array[current_index]
    max_index = left_index
  end
  if right_index <= end_index && array[right_index] > array[max_index]
    max_index = right_index
  end

  return unless max_index != current_index

  array[current_index], array[max_index] = array[max_index], array[current_index]
  max_heapify(array, max_index, end_index)
end

array = [3, 2, 1, 5, 6, 4, 8, 9, 7]
heap_sort(array)
puts array.join(',')
