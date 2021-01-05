class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            ans = int(str(x)[::-1])
        elif x <= 0:
            ans = -1 * int(str(x * -1) [::-1])
            
        min_ans = -2**31
        max_ans = 2**31 - 1
        
        if ans not in range(min_ans, max_ans):
            return 0
        else:
            return ans