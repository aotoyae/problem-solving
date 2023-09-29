const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let max = input[0];
let maxI = 0;

for (i = 0; i <= 9; i++) {
  if (max < input[i]) {
    max = input[i];
    maxI = i;
  }
}

console.log(max);
console.log(maxI + 1);
