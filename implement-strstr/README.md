# 28. Implement strStr()
## level: easy

https://leetcode.com/problems/implement-strstr/

```
strstr - locate a substring ( needle ) in a string ( haystack ).
```

Try not to use standard library string functions for this question.

Returns the index of the first occurrence of needle in haystack, or `-1` if needle is not part of haystack.

## Q. Good clarification questions

  - What should be the return value if the needle is empty?

  - What if both haystack and needle are empty?

For the purpose of this problem, assume that the return value should be -1 in both cases.

-------------------------------

## N gram index algorithm

This algorithm is easy to understand.
Make string index dictionary (like book indexes).

For example, the haystack is `HelloWorld`, and the needle is `World`.

if we choose `n = 1`, the dictionary becomes below:
```
{
 'H': [0],
 'e': [1],
 'l': [2, 3, 8],
 'o': [4, 6],
 'W': [5],
 'r': [7],
 'd': [9]
}
```

Or if we choose `n=2`, then

```
{
  'He': [0],
  'el': [1],
  'll': [2],
  'lo': [3],
  'oW': [4],
  'Wo': [5],
  'or': [6],
  'rl': [7],
  'ld': [8]
}
```

You can choose `n` what ever you want.

Then, we search on the needle.

```
World -> ['Wo', 'or', 'rl', 'ld']
```

We know the `Wo` stars at `5`.
So we just checked `haystack[5: 10] == B`.

The below is my code:
```python
class Solution:
    def makeNgramHash(self, A, n):
        mem = {}
        for i in range(0, len(A) - n + 1):
            key = A[i: i + n]
            if key not in mem:
                mem[key] = [i]
            else:
                mem[key].append(i)
        return mem

    # @param A : an string
    # @param B : an string
    # @return an integer
    def strStr(self, A, B):

        sizeA = len(A)
        sizeB = len(B)
        if sizeA == 0:
            if sizeB == 0:
                return 0
            else:
                return -1
        if sizeA < sizeB:
            return -1
        if sizeA == 1:
            if sizeB < 2 or A == B:
                return 0
            else:
                return -1

        n = max(sizeB >> 1, 1)
        mem = self.makeNgramHash(A, n)

        i = 0
        while(i <= sizeB - n):
            key = B[i: i + n]
            if (key in mem):
                for startPos in mem[key]:
                    if A[startPos: startPos + sizeB] == B:
                        return startPos
                del mem[key]
            i += 1

        return -1
```
