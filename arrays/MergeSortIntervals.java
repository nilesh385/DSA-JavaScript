/*
Merge and Sort Intervals
Given an array of intervals [startTime, endTime], merge all overlapping intervals and return a sorted array of non-overlapping intervals.

Example

Input

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output

[[1, 6], [8, 10], [15, 18]]
Explanation

- Step 1: Sort intervals by start time (already sorted). 
- Step 2: Initialize merged list with first interval [1,3]. 
- Step 3: Compare [2,6] with last merged [1,3]. They overlap (2 ≤ 3), so merge into [1,6]. Step 4: Compare [8,10] with last merged [1,6]. No overlap (8 > 6), append [8,10]. 
- Step 5: Compare [15,18] with last merged [8,10]. No overlap (15 > 10), append [15,18]. 

Result: [[1,6],[8,10],[15,18]].
Input Format

The first line contains an integer denoting the number of intervals.
The second line contains an integer denoting the length of individual interval array.
Each of the next N lines contains two space-separated integers startTime and endTime
Intervals may be provided in any order; duplicates and fully contained intervals are allowed.
Example

4
2
1 3
2 6
8 10
15 18
here, 4 is the number of intervals, 2 is the length of individual interval array, followed by the intervals.

Constraints

0 <= intervals.length <= 100000
intervals[i].length == 2 for all 0 <= i < intervals.length
0 <= intervals[i][0] < intervals[i][1] <= 10^9 for all 0 <= i < intervals.length
Output Format

Return a 2D array of two space-separated integers start and end, representing the merged intervals sorted by increasing start time.

*/

import java.util.ArrayList;
import java.util.List;

public class MergeSortIntervals {
    public static List<List<Integer>> main(List<List<Integer>> intervals) {
        // if there is only one interval
        if (intervals.isEmpty())
            return intervals;

        // Sorting the intervals in increasing order
        intervals.sort((a, b) -> Integer.compare(a.get(0), b.get(0)));

        List<List<Integer>> res = new ArrayList<>();
        res.add(intervals.get(0));

        for (int i = 1; i < intervals.size(); i++) {
            List<Integer> currentEle = intervals.get(i);
            List<Integer> prevEle = res.get(res.size() - 1); // it doesn't copy the value, it gives the direct reference
                                                             // of the last element

            if (currentEle.get(0) <= prevEle.get(1)) {
                // since ArrayList provides the direct reference to the element, we will just
                // change the end time
                prevEle.set(1, Integer.max(currentEle.get(1), prevEle.get(1)));
            } else {
                res.add(currentEle);
            }
        }

        return res;
    }
}
