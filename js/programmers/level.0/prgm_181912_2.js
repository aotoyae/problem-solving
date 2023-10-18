function solution(intStrs, k, s, l) {
  return intStrs.map((a) => +a.slice(s, s + l)).filter((a) => a > k);
}
