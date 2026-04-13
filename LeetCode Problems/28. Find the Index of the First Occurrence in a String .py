class Solution(object):
    def strStr(self, haystack, needle):
        """
        Returns the index of the first occurrence of needle in haystack,
        or -1 if needle is not part of haystack.
        """
        if not needle:
            return 0  # Edge case: empty needle

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

if __name__ == '__main__':
    solution = Solution()
    haystack1 = "sadbutsad"
    needle1 = "sad"
    print(solution.strStr(haystack1, needle1))  # Output: 0

    haystack2 = "leetcode"
    needle2 = "leeto"
    print(solution.strStr(haystack2, needle2))  # Output: -1
