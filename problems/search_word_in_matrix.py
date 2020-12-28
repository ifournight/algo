# encoding: UTF-8
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
# 示例:
#

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#
#
# 提示：
#
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-search
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        num_row = len(board)
        num_col = len(board[0])
        len_word = len(word)
        visited = [[False] * num_col for _ in range(num_row)]
        def dfs(b_index, w_index):
            """
            b_index 当前搜索的board索引
            w_index 当前搜索的word索引
            """
            r, c = b_index
            l_b = board[r][c]
            l_w = word[w_index]
            if visited[r][c] or l_b != l_w:
                return False
            if w_index + 1 == len_word:
                return True
            visited[r][c] = True
            if r != 0 and dfs((r - 1, c), w_index + 1):
                return True
            if c != 0 and dfs((r, c - 1), w_index + 1):
                return True
            if r != num_row - 1 and dfs((r + 1, c), w_index + 1):
                return True
            if c != num_col - 1 and dfs((r, c + 1), w_index + 1):
                return True
            visited[r][c] = False
            return False

        for r in range(num_row):
            for c in range(num_col):
                if dfs((r, c), 0):
                    return True
        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    match = Solution().exist(board, word)
    if match:
        print("In board {board} can find word {word}".format(
            board=board, word=word))
    else:
        print("No match")
