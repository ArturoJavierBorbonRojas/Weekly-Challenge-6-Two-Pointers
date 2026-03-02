# Weekly-Challenge-6-Two-Pointers
The challenge is to **reverse an array in-place**. While Python offers built-in methods like `.reverse()` or slicing `[::-1]`, implementing the logic from scratch demonstrates a deep understanding of index manipulation and memory management.


# ↔️ Week 6: Two Pointers Technique (Reverse Array In-Place)

## 📖 Description
For Week 6, I am exploring the **Two Pointers Technique**, a highly efficient algorithmic pattern used to solve array and string problems. 

The challenge is to **reverse an array in-place**. While Python offers built-in methods like `.reverse()` or slicing `[::-1]`, implementing the logic from scratch demonstrates a deep understanding of index manipulation and memory management.

## ⚙️ How it works
1. **Initialize:** We place one pointer at the beginning (`left = 0`) and one at the end (`right = len(arr) - 1`).
2. **Swap:** We swap the elements at these two indices.
3. **Move:** We move the `left` pointer forward (`left += 1`) and the `right` pointer backward (`right -= 1`).
4. **Terminate:** The loop stops when the pointers meet or cross in the middle (`left >= right`).

## 🚀 Complexity Analysis
* **Time Complexity:** $O(n)$ - Specifically $O(n/2)$, as we only need to iterate through half of the array to swap all elements. In Big O notation, constants are dropped, leaving us with linear time.
* **Space Complexity:** $O(1)$ - **Constant Space**. We are modifying the original array *in-place* without allocating memory for a new array.

## 💻 Code Snippet
```python
def reverse_in_place(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
        
    return nums
