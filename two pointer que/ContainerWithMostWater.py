'''
You're given a list of heights, height, one per vertical line, all
standing on the x-axis. Any two lines, together with the x-axis, form a
container.

Find the two lines that hold the most water, and return how much that container can hold.

Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
the lines at index 1 (height 8) and index 8 (height 7) are 7 apart, holding min(8,7) * 7 = 49
Input: height = [1, 1]
Output: 1
Constraints
2 <= height.length <= 10^5
0 <= height[i] <= 10^4
'''

def maxArea(height):
    mostW=0 # most water
    left=0
    right=len(height)-1

    while left<right:
        diff=(right-left)
        water= min(height[left],height[right])*diff
        mostW=max(mostW,water)
            
        if left<right and height[left]<height[right]:
            left+=1
        else:
            right-=1

    return mostW