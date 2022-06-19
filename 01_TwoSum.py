#Solves Two Sum Problem
# Use hash tables to store values for lookup
# have to return indices of nums that add to the target value
# [1, 2, 3, 4] target = 3 answer: [0,1]

def twoSum(nums,target):
    # initialiaze hash table
    hashtable = {}

    for i in range(len(nums)):
        # finds complement value for hash table
        complement = target - nums[i]
        if complement in hashtable:
            return (hashtable[complement],i) # returns ordered pair of index locations 
        hashtable[nums[i]] = i # stores value of nums and corresponding index in hash table (if num is 1 at index 0 it is stored as 1:0)

test = [1,3,2,4]
test_target = 3

twoSum(test,test_target)