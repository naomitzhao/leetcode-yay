class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        generated = set()

        def generate(remaining, currString):
            # print("starting at " + str(currString))
            if currString in generated:
                return 0
            generated.add(currString)
            count = 1
            for ch in list(remaining):
                currString += ch
                remaining[ch] -= 1
                if remaining[ch] == 0:
                    del remaining[ch]
                count += generate(remaining, currString)
                if ch in remaining:
                    remaining[ch] += 1
                else:
                    remaining[ch] = 1
                currString = currString[:-1]
            
            # print("starting at " + str(currString) + " got " + str(count))
            # print("\tgot " + str(count))
            return count
        
        initRemaining = {}
        for tile in tiles:
            if tile in initRemaining:
                initRemaining[tile] += 1
            else:
                initRemaining[tile] = 1
        
        return generate(initRemaining, "") - 1
