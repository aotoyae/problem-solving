function solution(s) {
  let num = Math.floor(s.length / 2);

  return s.length % 2 === 0 ? s.slice(num - 1, num + 1) : s[num];
}
