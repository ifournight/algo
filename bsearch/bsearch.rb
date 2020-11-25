def binary_search(array, n)
  low = 0
  high = array.size - 1
  mid = low + (high - low) / 2
  while low <= high
    if array[mid] < n
      low = mid + 1
    elsif array[mid] > n
      high = mid - 1
    else
      return mid
    end
    mid = low + (high - low) / 2
  end
  -1
end

array = [2, 3, 3, 3, 4, 5, 5, 8, 8]
array.sort!
puts array.join(',')
puts binary_search(array, 5)