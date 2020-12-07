def simple_arithmetic(expression):
  '''Given a simple arithemetic expression string and return calculated result,
     the expression string accept integer and ['+', '-', '*', '/'] operator, parethesis not allowed'''
  import re
  items = re.findall(r"\d+|\+|-|\*|\/", expression)
  print items
  all_operators = frozenset(['+', '-', '*', '/'])
  operator_priorities = { '+': 1, '-': 1, '*': 2, '/': 2 }
  numbers = []
  operators = []
  def subroutine():
    while len(operators) > 0 and (len(numbers) / 2) > 0:
      operator = operators.pop()
      n1, n2 = numbers[-2:]
      del numbers[-2:]
      n3 = arithmetic_helper(n1, n2, operator)
      numbers.append(n3)
  for item in items:
    if item.isdigit():
      numbers.append(int(item))
      if len(operators) >= 2 and operator_priorities[operators[-1]] >= operator_priorities[operators[-2]]:
        subroutine()
    elif item in all_operators:
      operators.append(item)
  subroutine()
  return numbers.pop()
    
def arithmetic_helper(n1, n2, operator):
  if operator == '+':
    return n1 + n2
  elif operator == '-':
    return n1 - n2
  elif operator == '*':
    return n1 * n2
  elif operator == '/':
    return n1 / n2
  else:
    return None

if __name__ == "__main__":
  
  def only_one_operator_test():
    print "test only one operator"
    exp = '1 + 5'
    print "result of {exp} is {result}".format(exp=exp,result=simple_arithmetic(exp))
  
  def simple_plus_minus_test():
    print "test simple plus and minus"
    exp = '1 + 5 - 3'
    print "result of {exp} is {result}".format(exp=exp,result=simple_arithmetic(exp))
    
  def operator_priority_test():
    print "test expression containing operators with different priorities"
    exp = '1 + 5 * 3 - 10'
    print "result of {exp} is {result}".format(exp=exp,result=simple_arithmetic(exp))

  only_one_operator_test()
  simple_plus_minus_test()
  operator_priority_test()