function solution(n) {
  let str = "수박".repeat(n / 2) + (n % 2 ? "수" : "");

  return str;
}
