class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        Nr = len(recipes)
        Ni = len(ingredients)
        Ns = len(supplies)
        
        adj = {recipes[i]: list(ingredients[i]) for i in range(Nr)}
        possible = {}
        supplies = set(supplies)
        
        
        def dfs(cr):
          if cr not in vis:
            vis[cr] = 1
            flag = True
            for ingredient in adj[cr]:
              if ingredient in supplies:
                continue
              elif ingredient in adj:
                dfs(ingredient)
                if ingredient not in possible:
                  flag = False
              else:
                flag = False
            if flag: 
              possible[cr] = 1
        
        
        for recipe in recipes:
          vis = {}
          dfs(recipe)
        
        return [x for x in possible]
            