function solution(n) {
  result = n.toString(3).split("").reverse().join("");

  return parseInt(result, 3);
}
