# frozen_string_literal: true

# 动态大小的小顶堆
# Author: ifournight
# Date: 2020-11-30
class MinHeap
  def initialize
    @heap = []
  end

  # 元素个数
  def size
    @heap.size
  end

  # 打印
  def to_str
    @heap.join(',')
  end

  # 插入
  def insert(key)
    @heap << key
    current_index = @heap.size - 1
    parent_index = (current_index - 1) / 2
    while parent_index >= 0 && @heap[current_index] < @heap[parent_index]
      swap(current_index, parent_index)
      current_index = parent_index
      parent_index = (parent_index - 1) / 2
    end
  end

  # 取除最小值
  def pop_min
    swap(0, @heap.size - 1)
    key = @heap.pop
    min_heapify(0)
    key
  end

  # 从大到小排序
  def heapsort
    # build_min_heap
    i = size - 1
    while i.positive?
      swap(0, i)
      i -= 1
      min_heapify(0, i)
    end
  end

  # 最小值
  def min
    @heap[0]
  end

  private

  # 建堆
  def build_min_heap
    last_parent_index = (size - 2) / 2
    start = last_parent_index
    while start >= 0
      min_heapify(start)
      start -= 1
    end
  end

  def min_heapify(current_index, end_index = nil)
    end_index ||= @heap.size - 1
    left_index = current_index * 2 + 1
    right_index = current_index * 2 + 2
    min_index = current_index
    if left_index <= end_index && @heap[left_index] < @heap[current_index]
      min_index = left_index
    end
    if right_index <= end_index && @heap[right_index] < @heap[min_index]
      min_index = right_index
    end
    if min_index != current_index
      swap(current_index, min_index)
      min_heapify(min_index, end_index)
    end
  end

  def swap(i, j)
    @heap[i], @heap[j] = @heap[j], @heap[i]
  end
end

heap = MinHeap.new
10.times { |_| heap.insert rand(20) }
puts heap.to_str
heap.heapsort
puts heap.to_str
# puts(heap.pop_min) while heap.size.positive?
# puts heap.to_str
