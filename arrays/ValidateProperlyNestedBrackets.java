/*
Validate Properly Nested Brackets
Given a string, check if all brackets ('()', '{}', '[]') are properly matched and nested. Return 1 if valid, otherwise return 0.

Example

Input

code_snippet = if (a[0] > b[1]) { doSomething(); }
Output

1
Explanation

All brackets are properly matched: '(' with ')', '[' with ']', and '{' with '}'. No mismatches or improper nesting.
Input Format

The function takes a single parameter, code_snippet, which is a STRING.
Constraints

0 <= code_snippet.length <= 1000
code_snippet consists of printable ASCII characters (character codes 32 to 126 inclusive)
code_snippet may contain any combination of '(', ')', '{', '}', '[', ']', letters, digits, symbols, and whitespace
code_snippet may be empty
Output Format

The function returns a BOOLEAN value, 1 for True and 0 for False.
*/

import java.util.Stack;

public class ValidateProperlyNestedBrackets {
    public static boolean main(String code_snippet) {
        if (code_snippet.isEmpty())
            return true;

        Stack<Character> brackets = new Stack<>();

        for (int i = 0; i < code_snippet.length(); i++) {
            Character ch = code_snippet.charAt(i);

            // add opening brackets
            if (ch == '(' || ch == '[' || ch == '{')
                brackets.add(ch);
            // handle closing brackets
            else if (ch == ')' || ch == ']' || ch == '}') {
                if (brackets.isEmpty())
                    return false;
                if (ch == ')' && brackets.peek() == '(' ||
                        ch == ']' && brackets.peek() == '['
                        || ch == '}' && brackets.peek() == '{')
                    brackets.pop();
                else
                    return false;
            } else
                continue;
        }

        return brackets.isEmpty();
    }
}
