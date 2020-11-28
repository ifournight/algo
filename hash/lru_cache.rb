# frozen_string_literal: true

# 双向链表的节点
class LinkNode
  attr_accessor :key, :value, :next_node, :prev_node

  # 初始化
  #
  # @param key
  # @param next_node
  # @param prev_node
  def initialize(key:, value:, next_node: nil, prev_node: nil)
    @key = key
    @value = value
    @next_node = next_node
    @prev_node = prev_node
  end

  # 断开连接
  def disconnect
    @next_node = nil
    @prev_node = nil
  end
end

# @Description: 基于散列表和双向链表实现的 LRU 缓存机制
# @Author: ifournight
# @Date: Create in 2020-11-28
# @Modified By:
# @Modified Date:
class LRUCache
  attr_reader :size

  MAX_CAPACITY = 10

  # 初始化
  def initialize
    @size = 0
    @table = {}
    @head = LinkNode.new(key: nil, value: nil)
    @tail = LinkNode.new(key: nil, value: nil)
    @head.next_node = @tail
    @tail.prev_node = @head
  end

  # 插入
  # @param key
  # @param value
  def put(key, value)
    if @table.key?(key)
      node = @table.fetch(key)
      node.value = value
      move_to_head(node)
    else
      if @size >= MAX_CAPACITY
        pop_tail
        @size -= 1
      end
      node = LinkNode.new(key: key, value: value)
      add_to_head(node)
      @size += 1
      @table[key] = node
    end
  end

  # 查找
  # @param key
  def get(key)
    return nil unless @table.key?(key)

    @table[key].value
  end

  # 删除
  # @param key
  def delete(key)
    return unless @table.key?(key)

    node = @table[key]
    remove_node(node)
    @size -= 1
    node.value
  end

  # 打印
  def to_str
    nodes = []
    curr = @head.next_node
    while curr && curr != @tail
      nodes << curr
      curr = curr.next_node
    end
    "LRU Cache size: #{size} #{nodes.map { |node| "#{node.key}/#{node.value}" }}.join('->')"
  end

  private

  # 将节点移动到链表头
  def move_to_head(node)
    remove_node(node)
    add_to_head(node)
  end

  # 从链表中删除节点
  def remove_node(node)
    node.prev_node.next_node = node.next_node
    node.next_node.prev_node = node.prev_node
    node.disconnect
    node
  end

  # 将节点插入链表头
  def add_to_head(node)
    node.prev_node = @head
    node.next_node = @head.next_node
    @head.next_node = node
    node.next_node.prev_node = node
  end

  # 从链表尾删除并返回节点
  def pop_tail
    node = @tail.prev_node
    remove_node(node)
    node
  end
end

cache = LRUCache.new
1.upto(10) do |num|
  cache.put(num, num)
  puts cache.to_str
end
puts cache.to_str
cache.put(5, 55)
puts cache.to_str
cache.put(11, 11)
cache.put(12, 12)
puts cache.to_str
cache.delete(6)
puts cache.to_str
