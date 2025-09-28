class Solution:
    def reverseWords(self, s: str) -> str:
        # i = 0
        # j = 0
        # print(s.split())
        # result = []
        # while len(s) > j:
        #     while j < len(s) and s[j] != ' ':
        #         j += 1
        #     if i != j:
        #         result.append(s[i:j])
        #         j += 1
        #         i = j
        #     else:
        #         i +=1
        #         j +=1
        
        # result.reverse()
        # return " ".join(result)
        print(s[::-1])
        list = s.split()
        return " ".join(list[::-1])
        
