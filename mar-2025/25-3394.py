class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        gaps = 0

        rectangles.sort()
        # print(rectangles)
        lastCol = rectangles[0][2]
        for i in range(1, len(rectangles)):
            if rectangles[i][0] >= lastCol:
                gaps += 1
            lastCol = max(lastCol, rectangles[i][2])

        # print(gaps)

        if gaps > 1:
            return True
        
        gaps = 0
        sortOther = sorted(rectangles, key=lambda rectangle: rectangle[1])
        # print(sortOther)
        lastRow = sortOther[0][3]
        for i in range(1, len(sortOther)):
            # print(sortOther[i][1], lastRow)
            if sortOther[i][1] >= lastRow:
                # print('\t', lastRow)
                gaps += 1
            lastRow = max(lastRow, sortOther[i][3])

        # print(gaps)

        return gaps > 1