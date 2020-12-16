# coding: UTF-8

# 给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
#
# 所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return "[.]".join(address.split("."))


if __name__ == "__main__":
    address = "255.100.50.0"
    print(Solution().defangIPaddr(address))
