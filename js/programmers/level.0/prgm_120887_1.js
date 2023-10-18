function solution(i, j, k) {
  let arr = "";
  for (i = i; i <= j; i++) {
    arr += i;
  }
  return arr.split(k).length - 1;
}
