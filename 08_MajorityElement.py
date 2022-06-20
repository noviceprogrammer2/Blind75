def majorityElement(nums):
    hashtable = {}
    
    if len(nums) == 1:
        return nums[0]
    for i in range(len(nums)):
        if nums[i] in hashtable:
            hashtable[nums[i]] += 1

        else:
            hashtable[nums[i]] = 1
    for key in hashtable:
        if hashtable[key] > len(nums)/2:
            return key 


majorityElement([6,6,6,7,7])