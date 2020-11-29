# frozen_string_literal: true

# 链表节点
class LinkNode
  attr_accessor :key, :next_node

  def initialize(key:, next_node: nil)
    @key = key
    @next_node = next_node
  end
end

# 单向链表
# @Author: ifournight
# @Date: Create in 2020-11-29
# @Modified By:
# @Modified Date:
class LinkedList
  attr_reader :size

  # 初始化
  def initialize
    @head = nil
    @size = 0
  end

  def to_str
    return '' if @head.nil?

    node = @head
    nodes = []
    while node
      nodes << node
      node = node.next_node
    end
    nodes.map(&:key).join('->')
  end

  # 根据 key 查找节点
  # @param key
  # @param node
  def find_by_key(key)
    return nil if @head.nil?

    node = @head
    node = node.next_node while node && node.key != key
    node
  end

  # 根据链表的 index 查找节点
  # @param index
  def find_by_index(index)
    return nil if @head.nil?

    i = 0
    node = @head
    while node && i != index
      node = node.next_node
      i += 1
    end
    node
  end

  # 将 key 插入到链表头
  # @param key
  def add_to_head(key)
    @head = if @head.nil?
              LinkNode.new(key: key)
            else
              LinkNode.new(key: key, next_node: @head)
            end
    @size += 1
  end

  # 将 key 插入到链表尾
  # @param key
  def add_to_tail(key)
    if @head.nil?
      @head = LinkNode.new(key: key)
    else
      node = @head
      node = node.next_node while node.next_node
      node.next_node = LinkNode.new(key: key)
    end
    @size += 1
  end

  # 删除一个尾元素并返回节点
  # @return tail node
  def pop_tail
    return nil if @head.nil?

    if @head.next_node.nil?
      node = @head
      @head = nil
      return node
    end

    before_node = @head
    node = @head.next_node
    while node.next_node
      before_node = node
      node = node.next_node
    end
    before_node.next_node = node.next_node
    @size -= 1
    node
  end

  # 将 key 插入到指定节点之后
  # @param node
  # @param key
  def insert_after(node:, key:)
    return if node.nil?

    new_node = LinkNode.new(key: key, next_node: node.next_node)
    node.next_node = new_node
    @size += 1
  end

  # 将 key 插入到指定节点之前
  # @param node
  # @param key
  def insert_before(node:, key:)
    return if node.nil?

    before_node = find_before(node)
    new_node = LinkNode.new(key: key, next_node: before_node.next_node)
    before_node.next_node = new_node
    @size += 1
  end

  # 把指定节点从链表中删除
  # @param node
  # @return node
  def delete_node(node)
    return nil if node.nil?

    if node == @head
      @head = nil
      @size -= 1
      return node
    end

    before_node = find_before(node)
    before_node.next_node = node.next_node
    node.next_node = nil
    @size -= 1
    node
  end

  # 根据 key 删除对应节点
  # @param key
  # @return node
  def delete_by_key(key)
    node = find_by_key(key)
    return nil unless node

    delete_node(node)
  end

  private

  # 找到上一节点
  # @param node
  # @param before node
  def find_before(node)
    return nil if @head.nil? || @head.next_node.nil?

    current = @head
    current = current.next_node while current && current.next_node != node
    current
  end
end

list = LinkedList.new
('a'..'f').each do |letter|
  list.add_to_tail(letter)
  puts list.to_str
end

('A'..'F').each do |letter|
  list.add_to_head(letter)
end
puts list.to_str
cap_d = list.find_by_index(2)
list.insert_after(node: cap_d, key: 'Dd')
puts list.to_str
d = list.find_by_key('d')
puts d.key
list.insert_before(node: d, key: 'cd')
puts list.to_str
list.pop_tail
puts list.to_str
list.pop_tail
puts list.to_str
puts list.size
