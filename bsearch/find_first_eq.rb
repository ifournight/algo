# frozen_string_literal: true

def find_first_eq(array, n)
  low = 0
  high = array.size - 1
  mid = low + (high - low) / 2
  while low <= high
    if array[mid] < n
      low = mid + 1
    elsif array[mid] > n
      high = mid - 1
    else
      return mid if mid.zero? || array[mid - 1] < n

      high = mid - 1
    end
    mid = low + (high - low) / 2
  end
  -1
end

def find_last_eq(array, n)
  low = 0
  high = array.size - 1
  mid = low + (high - low) / 2
  while low <= high
    if array[mid] < n
      low = mid + 1
    elsif array[mid] > n
      high = mid - 1
    else
      return mid if mid == (array.size - 1) || array[mid + 1] > n

      low = mid + 1
    end
    mid = low + (high - low) / 2
  end
  -1
end

def find_first_ge(array, n)
  low = 0
  high = array.size - 1
  mid = low + (high - low) / 2
  while low <= high
    if array[mid] >= n
      return mid if mid.zero? || array[mid - 1] < n

      high = mid - 1
    else
      low = mid + 1
    end
    mid = low + (high - low) / 2
  end
  -1
end

def find_last_le(array, n)
  low = 0
  high = array.size - 1
  mid = low + (high - low) / 2
  while low <= high
    if array[mid] <= n
      return mid if mid == array.size - 1 || array[mid + 1] > n

      low = mid + 1
    else
      high = mid - 1
    end
    mid = low + (high - low) / 2
  end
end

array = [2, 3, 3, 3, 4, 5, 5, 8, 8]
array.sort!
puts array.join(',')
puts find_first_eq(array, 5)
puts find_last_eq(array, 5)
puts find_first_ge(array, 6)
puts find_last_le(array, 6)
