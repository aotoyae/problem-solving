const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let firstNum = Number(input[0]);
let secondNum = Number(input[1]);
let primeArr = [];

for (i = firstNum; i <= secondNum; i++) {
  primeArr.push(i);
}
const answer = primeArr.filter((num) => {
  for (let j = 2; j < num; j++) {
    if (num % j === 0) {
      return false;
    }
  }
  return num > 1;
});

if (answer.length) {
  console.log(answer.reduce((a, b) => a + b));
  console.log(answer[0]);
} else {
  console.log(-1);
}
