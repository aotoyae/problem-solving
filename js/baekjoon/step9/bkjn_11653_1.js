const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let num = input;
let answer = [];

for (i = 2; i <= num; i++) {
  while (num % i === 0) {
    num = num / i;
    answer.push(i);
    console.log(i);
  }
}
