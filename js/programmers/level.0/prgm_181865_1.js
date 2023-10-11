function solution(binomial) {
  const [num1, op, num2] = binomial.split(" ");
  return op === "+" ? +num1 + +num2 : op === "-" ? num1 - num2 : num1 * num2;
}
