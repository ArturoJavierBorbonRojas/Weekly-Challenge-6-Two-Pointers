import numpy as np

# Weekly challenge 6: Two Pointers Technique (Reverse Array In-Place)
# Author: Ing. Arturo Javier Borbon Rojas

# 1. Generate a random list of numbers
n= np.random.randint(5,10)
print("Our n is: ", n)

# Tranform our numpy random list to native Python list for cleaner visual output
arr= np.random.randint(1,100, n).tolist()
print("Our original array is: ", arr)


def reverse_in_place(nums):
    # Initialize the two pointers
    left=0
    right= len(nums)-1
    step=1

    # Loop until the pointers meet or cross in the middle
    while left< right:
        print(f"Step {step}: Swapping {nums[left]} (idx {left}) with {nums[right]} (idx {right})")

    # The Swap Python makes it in a very elegant way, but you can also do it with a temporary variable if you prefer:
        nums[left], nums[right]= nums[right], nums[left]
        
        print(f"       Current state: {nums}")
        
        # Move the pointers towards the center
        left += 1
        right -= 1
        step += 1
        
    return nums


# 2. Execute
reversed_arr = reverse_in_place(arr)

print("--------------------------------------------------")
print(f" ✅ Final Reversed Array: {reversed_arr}")
print("--------------------------------------------------")