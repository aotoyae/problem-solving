function solution(order) {
  return [...String(order)].filter((a) => ["3", "6", "9"].includes(a)).length;
}
