def naive_string_match(main_str, pattern):
  '''naive way to implement string match method'''
  matches = []
  i = 0
  for i in range(0, len(main_str) - len(pattern) + 1):
    if main_str[i:len(pattern) + i] == pattern:
      matches.append(i)
    i += 1
  return matches
  
def less_naive_string_match(main_str, pattern):
  '''sligtly less naive way to implement string match'''
  # Generate characters set of pattern string
  pattern_set = set([char for char in pattern])
  matches = []
  i = 0
  while i <= len(main_str) - len(pattern):
    j = 0
    while j < len(pattern):
      # If mismatch happen, and mismatched character in main str does
      # not occur in pattern str, skip to position after mismatched index
      if main_str[i + j] != pattern[j] and \
         main_str[i + j] not in pattern_set:
        break
      j += 1
    if j == len(pattern):
      matches.append(i)
      i += 1
    else:
      i += j + 1
  return matches

if __name__ == "__main__":
  def test_match():
    print('test_match')
    pattern = 'ab'
    main_str = 'absence'
    print("find {pattern} in {main_str} at index {indices}".format(pattern = pattern, main_str = main_str, indices = less_naive_string_match(main_str, pattern)))
    
  def test_no_match():
    print('test no match')
    pattern = 'word'
    main_str = 'There would have been a time for such a word'
    print("find {pattern} in {main_str} at index {indices}".format(pattern = pattern, main_str = main_str, indices = less_naive_string_match(main_str, pattern)))
    
  def test_multi_matches():
    pattern = 'ab'
    main_str = 'absenabce'
    print("find {pattern} in {main_str} at index {indices}".format(pattern = pattern, main_str = main_str, indices = less_naive_string_match(main_str, pattern)))
    
  def test_subfix_matches():
    pattern = 'ce'
    main_str = 'absenabce'
    print("find {pattern} in {main_str} at index {indices}".format(pattern = pattern, main_str = main_str, indices = less_naive_string_match(main_str, pattern)))
    
  test_match()
  test_no_match()
  test_multi_matches()
  test_subfix_matches()
    
  

