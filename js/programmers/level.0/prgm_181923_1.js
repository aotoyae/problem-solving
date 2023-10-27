function solution(arr, queries) {
  let result = [];
  for (let [s, e, k] of queries) {
    let num = arr
      .filter((v, i) => i >= s && i <= e && v > k)
      .sort((a, b) => a - b)[0];
    result.push(num ? num : -1);
  }
  return result;
}
