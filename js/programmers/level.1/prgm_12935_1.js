function solution(arr) {
  let minNum = Math.min(...arr);
  let result = arr.filter((item) => item !== minNum);

  return result.length === 0 ? [-1] : result;
}
