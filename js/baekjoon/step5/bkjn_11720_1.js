const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let a = Number(input[0]);
let b = input[1].split("");
let sum = 0;

for (i = 0; i < a; i++) {
  sum += Number(b[i]);
}

console.log(sum);
