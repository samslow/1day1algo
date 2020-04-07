def hourglassSum(arr):
    sum_arr = []
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            hg_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            sum_arr.append(hg_sum)
        
    return max(sum_arr)