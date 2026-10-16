class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        while matrix:

            # 1 adding the first row/list of matrix
            res += (matrix.pop(0))

            # 2 append the last element of all lists in order
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            
            # 3 Adding reverse of last row/list
            if matrix:
                res += (matrix.pop()[::-1])
            
            # 4 Append the first element of all rows/lists in reverse
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        
        return res