# find_digits

## Problem

This is LeetCode problem [#321](https://leetcode.com/problems/create-maximum-number/).

> Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

>Example 1:<br/>
nums1 = [3, 4, 6, 5]<br/>
nums2 = [9, 1, 2, 5, 8, 3]<br/>
k = 5<br/>
return [9, 8, 6, 5, 3]<br/>

>Example 2:<br/>
nums1 = [6, 7]<br/>
nums2 = [6, 0, 4]<br/>
k = 5<br/>
return [6, 7, 6, 0, 4]<br/>

>Example 3:<br/>
nums1 = [3, 9]<br/>
nums2 = [8, 9]<br/>
k = 3<br/>
return [9, 8, 9]<br/>

## Observations / Explanation

* Given two lists of digits (i.e. `digits1` and `digits2`) with a random distribution, and a value of `k` that is much smaller than the total number of digits available in these lists, it is trivial to find the `9` digit `k` times, maximizing the resulting number.  The problem becomes interesting when the value of `k` is the same as or a little less than the total number of digits available in these lists.  At this point, choosing the wrong digit may mean running out of digits to construct a number with `k` digits, or the greatest digits not being maximally shifted to the left in the number as to maximize its value.

* In order to construct the number with the maximum value, starting the construction from the left, it is necessary to find the greatest available digit such that once consumed there will still be enough remaining digits to build a number with `k` digits and as to maximize subsequent digit choice.  For example, this means picking a `9` first if there will be enough remaining digits to build a number with `k` digits.  If a `9` can't be found given these constraints, then it is necessary to look for an `8`, and so forth.  Once a digit is found given these constraints, it is necessary to repeat the process for the next digit in the number being constructed starting once again from `9`.

* It may not seem important which digit is picked when encountering the same candidate digit in both lists.  However, consider the cases `digits1 = [6, 7]`, `digits2 = [6, 0, 4]`, `k = 5`, and `digits1 = [1, 1, 9, 1, 1]`, `digits2 = [1, 1, 1, 9, 1]`, `k = 6`.  The correct solutions for these inputs are `[6, 7, 6, 0, 4]` and `[9, 1, 9, 1, 1, 1]` respectively.  Notice in the first case that that the first digit of the result is `6`.  Is this the `6` at the beginning of the first or second list?  For the second case, the second digit of the result is `1`.  Is this this the `1` at the beginning of the first list or the `1` following the `9` in the second list?  In both cases, selecting the wrong candidate, `6` and `1` respectively, will result in one of the digits needed to get the correct result becoming unavailable.

* When encountering the same candidate in both lists, as just described, it is necessary to pick the candidate from the list that will still have a digit greater than the candidate digit once chosen.  In other words, given the remainder of the lists after picking the first `9` in the second case above as `digits1 = [1, 1, 9, 1, 1]`, `digits2 = [1]`, the `1` at the beginning of the first list must be picked because it is followed by `9`, a greater digit.  There is no such greater digit in the second list.

* If the candidate in both lists is followed by a greater digit, the correct digit choice will maximize the number of remaining digits relative to the position of the greater digit (i.e. maximize subsequent digit choice).

* It was discussed that all of these situations only apply when `k` minus the number of chosen digits equals the number of remaining digits.  This seems plausible, but I have not convinced myself that it is absolutely true.
