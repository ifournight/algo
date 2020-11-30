# frozen_string_literal: true
require_relative 'min_heap.rb'

n = 10_000_000
m = 100_000_000
k = 10
min_heap = MinHeap.new
n.times do
  num = rand(m)
  if min_heap.size < k
    min_heap.insert(num)
  elsif num > min_heap.min
    min_heap.pop_min
    min_heap.insert(num)
  end
end
puts "top 10 #{min_heap.to_str}"
