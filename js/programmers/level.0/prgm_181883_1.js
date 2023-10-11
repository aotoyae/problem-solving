function solution(arr, queries) {
  queries.map((a) => {
    for (i = a[0]; i <= a[1]; i++) {
      arr[i]++;
    }
  });
  return arr;
}
