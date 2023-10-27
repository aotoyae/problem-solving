function solution(arr, k) {
  let result = [...new Set(arr)];
  if (result.length > k) {
    while (result.length !== k) {
      result.pop();
    }
  } else {
    while (result.length !== k) {
      result.push(-1);
    }
  }
  return result;
}
