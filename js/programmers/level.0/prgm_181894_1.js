function solution(arr) {
  let start = arr.indexOf(2);
  let end = arr.lastIndexOf(2);

  return arr.includes(2) ? arr.slice(start, end + 1) : [-1];
}
