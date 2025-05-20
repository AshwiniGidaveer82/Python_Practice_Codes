class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                # Step 1: Get the encoded string inside [ ]
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()  # remove the '['

                # Step 2: Get the number (repeat count)
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                repeated = int(num) * substr
                stack.append(repeated)

        return ''.join(stack)
s = Solution()

print(s.decodeString("3[a]2[bc]"))        # Output: "aaabcbc"
print(s.decodeString("3[a2[c]]"))         # Output: "accaccacc"
print(s.decodeString("2[abc]3[cd]ef"))    # Output: "abcabccdcdcdef"
