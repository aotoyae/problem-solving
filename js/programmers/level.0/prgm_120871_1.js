function solution(n) {
  let result = 0;
  for (i = 1; i <= n; i++) {
    result++;
    while (String(result).includes("3") || result % 3 === 0) {
      result++;
    }
  }
  return result;
}
