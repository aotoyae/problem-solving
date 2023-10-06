function solution(array, n) {
  let count = array.filter((item) => item === n).length;
  return count;
}
