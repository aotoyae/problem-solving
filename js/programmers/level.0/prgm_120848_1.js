function solution(n) {
  let answer = 1;
  for (i = 1; i <= n; i++) {
    answer *= i;
    if (answer === n) {
      return i;
    } else if (answer > n) {
      return i - 1;
    }
  }
}
