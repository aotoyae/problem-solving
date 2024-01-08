function solution(x) {
  let [a, b] = String(x).split("");
  let numA = +a;
  let numB = +b;
  return x % (numA + numB) === 0 ? true : false;
}
