function check_sorted(arr)
{
    let flag = true;
    for (let i = 0; i < arr.length; i++)
    {
        if (arr[i] >= arr[i + 1])
        {
            flag = false;
            break;
        }
    }
    return flag;
}
function check_sorted_desc(arr)
{
    let res = check_sorted(arr);
    if (res == false)
    {
        console.log("Array is not sorted in ascending order");
    }
    else    
    {
        console.log("Array is sorted in ascending order");
    }
}
console.log(check_sorted_desc([1, 2, 3, 4, 5]));