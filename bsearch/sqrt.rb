# frozen_string_literal: true

require 'bigdecimal/util'

def sqrt(n)
  low = 0
  high = n
  mid = low + (high - low) / 2.to_d
  while (mid**2 - n).abs > 0.000001.to_d
    if mid**2 < n
      low = mid
    else
      high = mid
    end
    mid = low + (high - low) / 2.to_d
  end
  mid
end

puts sqrt(3)
puts sqrt(4)
puts sqrt(5)
puts sqrt(6)
puts sqrt(7)
puts sqrt(8)
puts sqrt(9)
