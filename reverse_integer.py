class Solution:
    def reverse(self, x: int) -> int:
        self.x = x
        
        if len(str(x)) == 1:
            return x
        
        int_list = list(str(x.__abs__()))
        int_list.reverse()
        x = int(''.join(int_list))

        if self.x < 0:
            x *= -1
            
        if x <= -2**31 or x >= 2**31 - 1:
            x = 0

        return x
        