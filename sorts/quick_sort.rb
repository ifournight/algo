# frozen_string_literal: true

def quick_sort(array)
  quick_sort_recurrsion(array, 0, array.size - 1)
end

def quick_sort_recurrsion(array, lower, upper)
  return if lower >= upper

  middle = partition(array, lower, upper)
  quick_sort_recurrsion(array, lower, middle - 1)
  quick_sort_recurrsion(array, middle + 1, upper)
end

def partition(array, lower, upper)
  r = upper
  pivot = array[r]
  i = lower
  lower.upto(upper - 1) do |j|
    if array[j] < pivot
      array[i], array[j] = array[j], array[i]
      i += 1
    end
  end
  array[i], array[r] = array[r], array[i]
  i
end

array = []
10.times { array << rand(100) }
quick_sort(array)
puts(array.join(','))
