nums=[1,2,3,4]
l_mul = 1
r_mul= 1
n=len(nums)
l_arr=[0]*n
r_arr=[0]*n

for i in range(n):
    j = -i-1
    l_arr[i] = l_mul
    l_mul *= nums[i]

    r_arr[j] = r_mul
    r_mul *= nums[j]
    print(l_arr)   
    print(r_arr)   

print (list(l*r for l,r in zip(l_arr,r_arr) ))