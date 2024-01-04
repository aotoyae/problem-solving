function solution(arr) {
  let num = 0;
  for (let i of arr) {
    num += i;
  }
  return num / arr.length;
}
