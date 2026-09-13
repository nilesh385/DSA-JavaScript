/*

Implement a stack that supports push, pop, top, and getMin operations in O(1) time, where getMin returns the minimum element.

Example

Input

n = 10
operations = ['push 2', 'push 0', 'push 3', 'push 0', 'getMin', 'pop', 'getMin', 'pop', 'top', 'getMin']
Output

[0,0,0,0]
Explanation

- push 2 → stack = [2], min = 2 2. 
- push 0 → stack = [2,0], min = 0 3.
- push 3 → stack = [2,0,3], min = 0 4. 
- push 0 → stack = [2,0,3,0], min = 0 5. 
- getMin → returns 0 6. 
- pop → removes 0, stack = [2,0,3], min = 0 7. 
- getMin → returns 0 8. 
- pop → removes 3, stack = [2,0], min = 0 9. 
- top → returns 0 10. getMin → returns 0
Input Format

operations: array of n number of operations, each matching exactly one of:
"push x" where x is an integer and 0 <= x <= 100
"pop"
"top"
"getMin"
The next n lines contain the value of elements in the array.
At any point in the sequence, the number of "pop" operations performed so far must be strictly less than the number of preceding "push" operations (so that the stack is never empty when "pop", "top", or "getMin" is called).
Constraints

For each "push x" operation, 0 <= x <= 100 and x is an integer
Each entry in operations must match the pattern ^(push \d+|pop|top|getMin)$
pop, top, and getMin operations are only invoked when the stack is non-empty
Total number of push operations <= n where n is the length of operations array
Output Format

An integer array of length equal to the total number of "top" and "getMin" operations in the input
*/

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class MinTrackingStack {
    public static List<Integer> main(List<String> operations) {
        Stack<Integer> stack = new Stack<>();
        List<Integer> res = new ArrayList<>();
        int minVal = Integer.MAX_VALUE;
        int top = 0;

        for (int i = 0; i < operations.size(); i++) {
            String operation = operations.get(i).substring(0, 4).toLowerCase().trim();
            int num = 0;
            if (operation.equalsIgnoreCase("push"))
                num = Integer.parseInt(operations.get(i).substring(5));

            if (operation.equalsIgnoreCase("push")) {
                if (stack.isEmpty())
                    top = num;

                stack.push(num);
                minVal = Integer.min(num, minVal);
            } else if (operation.equalsIgnoreCase("pop")) {
                if (!stack.isEmpty()) {
                    stack.pop();
                }

                if (!stack.isEmpty())
                    top = stack.peek();

            } else if (operation.equalsIgnoreCase("top"))
                res.add(top);
            else
                res.add(minVal);
        }

        return res;
    }
}
