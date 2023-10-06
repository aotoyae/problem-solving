function solution(strArr) {
  return strArr.map((a, i) => (i % 2 ? a.toUpperCase() : a.toLowerCase()));
}
