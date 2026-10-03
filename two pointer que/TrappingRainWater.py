'''
You're given a list of bar heights forming an elevation map, one unit wide each. After it rains, water gets trapped between the bars.

Return the total amount of water trapped.

Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
Input: height = [4, 2, 0, 3, 2, 5]
Output: 9
Constraints
0 <= height.length <= 2 * 10^4
0 <= height[i] <= 10^5
'''

def trappingRainWater(height):
    res=0

    for i in range(1,len(height)-1):
        #find the max num to the left side
        leftMax= max(height[:i])
        #find the max num to the right side
        righttMax= max(height[i+1:])

        water= max(0,min(leftMax,righttMax)-height[i])

        res+=water

    return res

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(trappingRainWater(height))
height = [4, 2, 0, 3, 2, 5]
print(trappingRainWater(height))