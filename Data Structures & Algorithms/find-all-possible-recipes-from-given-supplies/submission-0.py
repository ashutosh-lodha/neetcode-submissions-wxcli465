class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        suppliesSet = set(supplies)
        res = []
        for i in range(len(recipes)):
            allsupply = True
            for ingredient in ingredients[i]:
                if ingredient not in suppliesSet:
                    allsupply = False
            if allsupply:
                suppliesSet.add(recipes[i])
                res.append(recipes[i])
        
        return res
            
