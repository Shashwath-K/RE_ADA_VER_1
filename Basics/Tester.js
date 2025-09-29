function recursiveAlternatePrint(arr, startIndex)
{
    if (startIndex >= arr.length)
    {
        return;
    }
    console.log(arr[startIndex] += " ");
    recursiveAlternatePrint(arr, startIndex + 2);
}
let arr1 = [10, 20, 30, 40, 50, 60];
console.log("The alternate elements in the array using recursion are: \n");
recursiveAlternatePrint(arr1, 0);