class solution () :
    def twoSum (nums, target) :
        a = target
        o = []
        for i in range (0,len(nums)):
            for j in range (i+1,len(nums)):
                x = nums[i]+nums[j]
                if x == a:
                    o.append (i)
                    o.append (j)
                else :
                    pass
        print (o)


nums = []
nums = eval (input ("enter no in list"))
target = int (input ("enter target"))
obj = solution ()
obj.twoSum (nums,target)
