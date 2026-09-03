class Solution:
    def countSeniors(self, details: List[str]) -> int:
        total = 0
        for info in details:
            age = info[-4:-2]
            if int(age) > 60:
                total +=1
        return total