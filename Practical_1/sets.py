def find_combinations_of_three(nums, target_val):
    nums = list(set(nums))
    
    result = set()
    
    # Iterate through the indices of 'nums' to consider pairs of numbers.
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            # Calculate the third number ('complement') needed to reach the 'target_val'.
            complement = target_val - nums[i] - nums[j]
            
            # Check if the 'complement' exists in the remaining part of the list 'nums'.
            if complement in nums[:i] + nums[j+1:]:
                # Add a sorted tuple of the three numbers to the 'result' set.
                print(sorted((nums[i], nums[j], complement)))
                result.add(tuple(sorted((nums[i], nums[j], complement))))
    
    return list(result)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_val = 12
print("Original list of numbers:")
print(nums)
print("Target value:", target_val)

print("Combine three numbers whose sum equals the target number:")
print(find_combinations_of_three(nums, target_val))

target_val = 17
print("\nOriginal list of numbers:")
print(nums)
print("Target value:", target_val)

print("Combine three numbers whose sum equals the target number:")
print(find_combinations_of_three(nums, target_val))