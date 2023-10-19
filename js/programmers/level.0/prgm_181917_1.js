function solution(x1, x2, x3, x4) {
  let a = 0;
  let b = 0;
  if (x1 === true || x2 === true) {
    a = 1;
  }
  if (x3 === true || x4 === true) {
    b = 1;
  }
  return a === 1 && b === 1 ? true : false;
}
