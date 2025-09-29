function alternateArrayPrint(arr)
{
    console.log("The alternate elements in the array are: \n");
    for (let i = 0; i < arr.length; i += 2)
    {
        console.log(arr[i] + " ");
    }
}
let arr = [1, 2, 3, 4, 5, 6];
alternateArrayPrint(arr);