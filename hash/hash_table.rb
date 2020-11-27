# frozen_string_literal: true

# 散列表节点，有 next_entry 指向解决散列冲突链表的下一节点
class Entry
  attr_accessor :key, :value, :next_entry
  def initialize(key:, value:, next_entry: nil)
    @key = key
    @value = value
    @next_entry = next_entry
  end
end

# @Description:散列表实现
# @Author: ifournight
# @Date: Create in 2020-11-27
# @Modified By:
# @Modified Date:
class HashTable
  # 初始容量
  DEFAULT_INIT_CAPACIITY = 8

  # 装载因子
  LOAD_FACTOR = 0.75

  attr_reader :size

  def initialize
    # 实际使用量
    @size = 0
    # 数组索引使用量
    @use = 0
    # 数组
    @table = Array.new(DEFAULT_INIT_CAPACIITY)
  end

  # 新增

  # @param key
  # @param value
  def put(key, value)
    index = hash(key)
    # 设置哨兵节点
    @table[index] = Entry.new(key: nil, value: nil) if @table[index].nil?

    # 新增节点
    if @table[index].next_entry.nil?
      @table[index].next_entry = Entry.new(key: key, value: value)
      @use += 1
      @size += 1
      resize if @use >= @table.size * LOAD_FACTOR
    # 解决散列表冲突
    else
      tmp = @table[index].next_entry
      while tmp
        if tmp.key == key
          # 找到元素，更新值
          tmp.value = value
          return
        end
        tmp = tmp.next_entry
      end
      # 链表中未找到元素，插入链表头
      @table[index].next_entry = Entry.new(key: key, value: value, next_entry: @table[index].next_entry)
      @size += 1
    end
  end

  # 查找

  # @param key
  # @return value
  def get(key)
    index = hash(key)
    return nil if @table[index].nil?

    tmp = @table[index]
    while tmp
      return tmp.value if tmp.key == key

      tmp = tmp.next_entry
    end
    nil
  end

  # 删除
  # @param key
  def delete(key)
    index = hash(key)
    return if @table[index].nil?

    tmp = @table[index]
    while tmp&.next_entry
      # prev.next = curr.next
      if tmp.next_entry.key == key
        tmp.next_entry = tmp.next_entry.next_entry
        @use -= 1
        @size -= 1
      end

      tmp = tmp.next_entry
    end
  end

  # 打印
  def to_str
    nodes = []
    @table.each do |entry|
      tmp = entry
      while tmp
        nodes << tmp if tmp.key
        tmp = tmp.next_entry
      end
    end
    str = nodes.map { |node| "#{node.key} => #{node.value}" }.join(', ')
    "{ #{str} }"
  end

  # 解释
  def explain
    @table.each do |entry|
      if entry.nil?
        puts '[nil]'
        next
      end
      nodes = []
      tmp = entry
      while tmp
        nodes << tmp if tmp.key
        tmp = tmp.next_entry
      end
      puts "[#{nodes.map { |node| "[#{node.key}=>#{node.value}]" }.join('->')}]"
    end
    puts "Table size #{size} #{@use}/#{@table.size} alpha: #{@use / @table.size.to_f}"
  end

  private

  # 扩容
  def resize
    # 确保rehash时，size和table已经更新
    old_table = @table
    @use = 0
    @size = 0
    @table = Array.new(@table.size * 2)
    old_table.each do |dummy|
      next if dummy.nil? || dummy.next_entry.nil?

      tmp = dummy.next_entry
      while tmp
        put(tmp.key, tmp.value)
        tmp = tmp.next_entry
      end
    end
  end

  # 散列函数
  def hash(key)
    return 0 if key.nil?

    hash_code = key.hash
    (hash_code ^ (hash_code >> 16)) % @table.size
  end
end

hash_table = HashTable.new
hash_table.explain
'a'.upto('z').each { |letter| hash_table.put(letter, letter) }
hash_table.explain
puts hash_table.to_str
[%w[a b], %w[b c]].each { |pair| hash_table.put(pair.first, pair.last) }
puts hash_table.to_str
'a'.upto('g').each { |letter| hash_table.delete(letter) }
hash_table.explain
puts hash_table.to_str
