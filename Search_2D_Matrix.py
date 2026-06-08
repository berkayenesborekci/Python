class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        low = 0
        high = (m * n) - 1
        
        while low <= high:
            mid = (low + high) // 2 
            row = mid // n
            col = mid % n
            
            mid_element = matrix[row][col]
            
            if mid_element == target:
                return True
            elif mid_element < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
    
# Example usage:
# matrix = [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 60]
# ]
# target = 3
# solution = Solution()
# print(solution.searchMatrix(matrix, target))  # Output: True