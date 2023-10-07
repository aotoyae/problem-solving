function solution(n) {
  let answer = 0;
  if (n % 2 === 0) {
    for (i = 1; i <= n; i++) {
      i % 2 === 0 ? (answer += i * i) : 0;
    }
  } else {
    for (i = 1; i <= n; i++) {
      i % 2 === 1 ? (answer += i) : 0;
    }
  }
  return answer;
}
