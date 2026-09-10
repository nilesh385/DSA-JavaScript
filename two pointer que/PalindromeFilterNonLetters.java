/*
Check Palindrome by Filtering Non-Letters
Given a string containing letters, digits, and symbols, determine if it reads the same forwards and backwards when considering only alphabetic characters (case-insensitive).

Example

Input

code = A1b2B!a
Output

1
Explanation

- Step 1: Extract only letters → ['A','b','B','a'] 
- Step 2: Convert to lowercase → ['a','b','b','a'] 
- Step 3: Compare sequence forward and backward: 'abba' == 'abba' → true
Input Format

A string code containing letters (A–Z, a–z), digits (0–9), and symbols
Constraints

0 <= code.length <= 1000
For all 0 <= i < code.length: 33 <= ASCII(code[i]) <= 126
code contains only printable ASCII characters (letters, digits, symbols)
Output Format

Return a boolean value: 1 if true & 0 if false.
*/
public class PalindromeFilterNonLetters {

    public static boolean main(String code) {

        int left = 0;
        int right = code.length() - 1;

        while (left < right) {
            while (left < right && !((code.charAt(left) >= 'A' && code.charAt(left) <= 'Z')
                    || (code.charAt(left) >= 'a' && code.charAt(left) <= 'z')))
                left++;
            while (left < right && !((code.charAt(right) >= 'A' && code.charAt(right) <= 'Z')
                    || (code.charAt(right) >= 'a' && code.charAt(right) <= 'z')))
                right--;

            if (Character.toLowerCase(code.charAt(left)) != Character.toLowerCase(code.charAt(right)))
                return false;

            left++;
            right--;

        }

        return true;
    }

}
