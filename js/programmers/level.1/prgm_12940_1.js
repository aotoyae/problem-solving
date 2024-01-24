function solution(n, m) {
  let lcm = 1;

  while (true) {
    if (lcm % n === 0 && lcm % m === 0) break;
    lcm++;
  }
  return lcm;
}
