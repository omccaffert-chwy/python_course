class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            first_number = i
            seek_number = target - nums[i]
            print(f"Seek number is {seek_number}")
            for i in range(len(nums)):
                second_number = i
                if nums[i] == seek_number and first_number != second_number:
                    return [first_number, second_number]
                    

            
        