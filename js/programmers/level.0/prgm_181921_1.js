function solution(l, r) {
  let result = [];
  for (i = l; i <= r; i++) {
    let num = String(i);
    if ([...num].every((x) => x === "5" || x === "0")) result.push(i);
  }
  return result.length ? result : [-1];
}
