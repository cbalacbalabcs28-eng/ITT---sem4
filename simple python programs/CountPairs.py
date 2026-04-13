def CountPairs(arr, target):
    a = len(arr)
    count = 0
    a=len(arr)
    for i in range(a):
        for j in range(i+1,a):
            if arr[i]+arr[j] == target:
                count+=1
    return(count)
if __name__ == "main":
    arr=[2,7,11,15]
    target=9
    print(CountPairs(arr,target))
