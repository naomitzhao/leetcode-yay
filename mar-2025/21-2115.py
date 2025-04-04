class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipeQueue = deque(range(len(recipes)))
        made = set(supplies)
        recipesMade = set()

        madeThisLoop = -1
        while madeThisLoop != 0:
            madeThisLoop = 0
            
            lenQ = len(recipeQueue)
            for i in range(lenQ):
                recipeIdx = recipeQueue.popleft()
                makeable = True
                for ingredient in ingredients[recipeIdx]:
                    if ingredient not in made:
                        makeable = False
                        break
                
                if makeable:
                    made.add(recipes[recipeIdx])
                    recipesMade.add(recipes[recipeIdx])
                    madeThisLoop += 1
                else:
                    recipeQueue.append(recipeIdx)
        
        return list(recipesMade)