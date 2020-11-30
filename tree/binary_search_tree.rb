# frozen_string_literal: true

# 二叉树节点
class BSTNode
  attr_accessor :key, :value, :left, :right, :parent

  def initialize(key:, value:)
    @key = key
    @value = value
    @root = nil
    disconnect
  end

  def disconnect
    @left = nil
    @right = nil
    @parent = nil
  end

  def to_str
    "#{key}=>#{value}"
  end
end

# 二叉树
# @author: ifournight
# @date: 2020-11-29
class BST
  # 初始化
  def initialize
    @root = nil
  end

  # 打印
  def to_str
    return '<empty tree>' if @root.nil?

    to_str_helper(@root)[0].join("\n")
  end

  # Copy from BST implementation from ⬇️
  # https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/readings/binary-search-trees/
  def to_str_helper(node)
    return [[], 0, 0] if node.nil?

    label = node.key.to_s
    left_lines, left_pos, left_width = to_str_helper(node.left)
    right_lines, right_pos, right_width = to_str_helper(node.right)
    middle = [right_pos + left_width - left_pos + 1, label.size, 2].max
    pos = left_pos + middle / 2
    width = left_pos + middle + right_width - right_pos
    left_lines << (' ' * left_width) while left_lines.size < right_lines.size
    right_lines << (' ' * right_width) while right_lines.size < left_lines.size
    if (middle - label.size).odd? && node.parent && node == node.parent.left && label.size < middle
      label += '.'
    end
    label = label.center(middle, '.')
    label[0] = ' ' if label[0] == '.'
    label[-1] = ' ' if label[-1] == '.'
    lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
             ' ' * left_pos + '/' + ' ' * (middle - 2) + '\\' + ' ' * (right_width - right_pos)]
    extras = left_lines.zip(right_lines).map do |left_line, right_line|
      left_line + ' ' * (width - left_width - right_width) + right_line
    end
    lines += extras
    [lines, pos, width]
  end

  private_methods :to_str_helper

  # 高度
  def height
    get_subtree_height(@root)
  end

  # 子树高度
  def get_subtree_height(node)
    return -1 if node.nil?

    [node.left, node.right].map { |child| get_subtree_height(child) }.max + 1
  end

  # 查找 key
  # @param key
  # @return node or nil
  def find(key)
    find_node_from(key: key, node: @root)
  end

  # 插入 k,v
  # @param key
  # @param value
  def insert(key:, value:)
    if @root.nil?
      @root = BSTNode.new(key: key, value: value)
      return
    end
    insert_from(key: key, value: value, node: @root)
  end

  # 删除
  # @param key
  def delete(key)
    node = find(key)
    delete_node(node)
  end

  # 删除节点
  # @param node
  def delete_node(node)
    return if node.nil?

    if node.left.nil?
      transplant(node: node, new_node: node.right)
    elsif node.right.nil?
      transplant(node: node, new_node: node.left)
    else
      successor = successor(node)
      if successor.parent != node
        transplant(node: successor, new_node: successor.right)
        successor.right = node.right
        node.right.parent = successor
      end
      transplant(node: node, new_node: successor)
      successor.left = node.left
      node.left.parent = successor
    end
    node.disconnect
  end

  # 最小节点
  def min
    find_min_from(@root)
  end

  # 最大节点
  def max
    find_max_from(@root)
  end

  # 下一个节点
  # @param node
  # @return successor node
  def successor(node)
    return nil if node.nil?
    return find_min_from(node.right) if node.right

    # find lowest ancestor whose left child is also a ancestor
    current = node
    parent = node.parent
    while parent && current != parent.left
      current = parent
      parent = parent.parent
    end
    parent # can be nil
  end

  # 上一个节点
  # @param node
  # @return predecessor node
  def predecessor(node)
    return nil if node.nil?
    return find_max_from(node.left) if node.left

    # find lowest ancestor whose right child is also an ancestor
    _current = node
    parent = node.parent
    while parent && parent != parent.right
      _current = parent
      parent = parent.parent
    end
    parent # can be nil
  end

  # 返回按层级遍历的节点数列
  def collect_bfs
    bfs = []
    level = [@root]
    depth = 0
    while level.size.positive?
      next_level = []
      level.each do |node|
        bfs << [node, depth]
        next_level += [node.left, node.right].compact
      end
      level = next_level
      depth += 1
    end
    bfs
  end

  # 返回中序遍历顺序的节点数列
  def collect_inorder
    inorder = []
    stack = []
    current = [@root, 0]
    loop do
      if current && current[0]
        stack << current
        node, depth = current
        current = [node.left, depth + 1]
      elsif stack.size.positive?
        current = stack.pop
        inorder << current
        node, depth = current
        current = [node.right, depth + 1]
      else
        break
      end
    end
    inorder
  end

  # 返回先序遍历顺序的节点数列
  def collect_preorder
    preorder = []
    stack = [[@root, 0]]
    while stack.size.positive?
      current = stack.pop
      preorder << current
      node, depth = current
      stack << [node.right, depth + 1] if node.right
      stack << [node.left, depth + 1] if node.left
    end
    preorder
  end

  # 返回后续遍历顺序的节点数列
  def collect_postorder
    postorder = []
    stack = [[@root, 0]]
    while stack.size.positive?
      current = stack.pop
      postorder << current
      node, depth = current
      stack << [node.left, depth + 1] if node.left
      stack << [node.right, depth + 1] if node.right
    end
    postorder.reverse
  end

  private

  # 从指定节点开始找最小值
  def find_min_from(node)
    current = node
    current = current.left while current&.left
    current # can be nil
  end

  # 从指定节点开始找最大值
  def find_max_from(node)
    current = node
    current = current.right while current&.right
    current # can be nil
  end

  # 从指定节点开始查找 key
  # @param key
  # @param node
  # @return node or nil
  def find_node_from(key:, node:)
    return nil if node.nil?

    current = node
    while current
      return current if key == current.key

      current = key < current.value ? current.left : current.right
    end
    current # can be nil
  end

  # 在指定节点开始插入 k, v
  # @param key
  # @param value
  # @param node
  def insert_from(key:, value:, node:)
    return if node.nil?

    new_node = BSTNode.new(key: key, value: value)
    current = node
    while current
      if key < current.value
        if current.left.nil?
          current.left = new_node
          new_node.parent = current
          return
        end
        current = current.left
      else
        if current.right.nil?
          current.right = new_node
          new_node.parent = current
          return
        end
        current = current.right
      end
    end
  end

  # 把新节点移植到指定节点的位置
  def transplant(node:, new_node:)
    if node.parent.nil?
      @root = new_node
    elsif node.parent.left == node
      node.parent.left = new_node
    else
      node.parent.right = new_node
    end
    new_node.parent = node.parent if new_node
  end
end

bst = BST.new
puts "bst height #{bst.height}"
[3, 2, 1, 4, 5].each { |num| bst.insert(key: num, value: num) }
puts bst.to_str
puts '---------'
puts bst.min.value
puts bst.max.value
bst.insert(key: 6, value: 6)
puts bst.to_str
puts '---------'
puts "bst height #{bst.height}"
puts bst.to_str
puts '---------'
bst.delete(6)
puts bst.to_str
puts '---------'
bst.delete_node bst.min
bst.delete_node bst.max
puts bst.to_str
puts '---------'

bst = BST.new
[1, 4, 9, 5, 6, 10, 8, 12].each { |num| bst.insert(key: num, value: num) }
puts bst.to_str
puts '---------'
bst.delete(9)
puts bst.to_str
puts '---------'
inorder = bst.collect_inorder.map { |node, depth| "#{node.key}{#{depth}}" }.join(',')
puts "inorder #{inorder}"
preorder = bst.collect_preorder.map { |node, depth| "#{node.key}{#{depth}}" }.join(',')
puts "preorder #{preorder}"
postorder = bst.collect_postorder.map { |node, depth| "#{node.key}{#{depth}}" }.join(',')
puts "postorder #{postorder}"
bfs = bst.collect_bfs.map { |node, depth| "#{node.key}{#{depth}}" }.join(',')
puts "bfs #{bfs}"
puts '---------'

bst = BST.new
[33, 16, 13, 15, 18, 50, 25, 17, 27, 19, 58, 34, 51, 55, 66].each { |num| bst.insert(key: num, value: num) }
puts "bst height #{bst.height}"
puts bst.to_str
puts '---------'
bst.delete(13)
puts 'delete 13'
puts bst.to_str
puts '---------'
bst.delete(18)
puts 'delete 18'
puts bst.to_str
puts '---------'
bst.delete(55)
puts 'delete 55'
puts bst.to_str
puts '---------'
puts "bst height #{bst.height}"
