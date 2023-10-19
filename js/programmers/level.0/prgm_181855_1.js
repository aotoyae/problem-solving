function solution(strArr) {
  const result = {};
  const maxLength = Math.max(...strArr.map((a) => a.length));

  for (i = 1; i <= maxLength; i++) {
    const obj = strArr.filter((a) => a.length === i);
    result[i] = obj.length;
  }
  return Math.max(...Object.values(result));
}
