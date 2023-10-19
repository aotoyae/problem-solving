function solution(arr) {
  let result = 0;
  let copyArr = arr;
  while (true) {
    const changeArr = copyArr.map((a) => {
      if (a >= 50 && a % 2 === 0) return a / 2;
      if (a < 50 && a % 2 === 1) return a * 2 + 1;
      return a;
    });
    const checkArr = copyArr.every((a, i) => a === changeArr[i]);
    if (checkArr) break;
    result++;
    copyArr = changeArr;
  }
  return result;
}
