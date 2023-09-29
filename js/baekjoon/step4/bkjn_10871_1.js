const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let firstLine = input[0].split(" ");
let n = Number(firstLine[0]);
let x = Number(firstLine[1]);
let secondLine = input[1].split(" ");
const result = "";

for (i = 0; i < n; i++) {
  if (x > secondLine[i]) {
    result += secondLine[i] + " ";
  }
}
console.log(result);
