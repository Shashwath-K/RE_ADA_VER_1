function make_evn(arr)
{
    let n = arr.length;
    for (let i = 1; i < n; i++)
    {
        if((i+1)%2 == 0)
        {
            if(arr[i] < arr[i+1])
            {
                let temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
            }
        }
        else
        {
            if(arr[i] > arr[i+1])
            {
                let temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
            }
        }
    }
}
console.log("Make even positioned elements greater than odd positioned elements");
let arr = [1, 3, 2, 2, 5];
make_evn(arr);
console.log(arr);
// Output: [3, 1, 5, 2, 2]