function solution(n) {
  let count = 0;

  for (i = 2; i <= n; i += 2) {
    count += i;
  }

  return count;
}
