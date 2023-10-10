function solution(a, b) {
  return +(String(a) + String(b)) >= 2 * a * b
    ? +(String(a) + String(b))
    : 2 * a * b;
}
