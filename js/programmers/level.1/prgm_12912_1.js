// 이 방법이 더 빠르다
function solution(a, b) {
  let num = 0;
  if (a < b) {
    for (let i = a; i <= b; i++) {
      num += i;
    }
  } else {
    for (let i = b; i <= a; i++) {
      num += i;
    }
  }
  return num;
}
