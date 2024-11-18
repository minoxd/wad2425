function findMax(arr) {
    if (arr.length === 0) alert('empty array');
    let max = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (max<arr[i]) max = arr[i];
    }
    alert(max);
}
findMax([1,2,3,4,5,6,7,8,9]);
findMax([]);