function solution(arr, k) {
  if (k % 2 === 1) {
    return arr.map((a) => a * k);
  } else if (k % 2 === 0) {
    return arr.map((a) => a + k);
  }
  // 한 줄로 가능
  // return arr.map((a) => (k % 2 ? a * k : a + k));
}
