class Solutions:
    def maxArea(self, heights: list[int]) -> int:
        maxArea = 0  # Intializing the max area to be 0
        # Intializing the 2D array to store the values => (index, height)
        stack = []
        # Transversing through the list given
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                stackI, stackH = stack.pop()
                maxArea = max(maxArea, stackH*(index-stackI))
                start = stackI
            stack.append((start, height))
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea


object1 = Solutions()
print(object1.maxArea([2, 1, 5, 6, 2, 3]))
