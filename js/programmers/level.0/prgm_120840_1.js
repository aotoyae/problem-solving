function solution(balls, share) {
  return factorial(balls) / (factorial(balls - share) * factorial(share));
}
function factorial(n) {
  let returnFacto = BigInt(1);
  for (i = n; i >= 2; i--) {
    returnFacto *= BigInt(i);
  }
  return returnFacto;
}
