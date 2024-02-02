function solution(s) {
  let result = [];

  for (let i = 0; i < s.length; i++) {
    const arr = s.slice(0, i);
    const idx = arr.lastIndexOf(s[i]);
    if (idx === -1) {
      result.push(-1);
    } else {
      result.push(i - idx);
    }
  }

  return result;
}
