const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let n = Number(input[0]);
let arr = input[1].split(" ").map(Number);

let max = arr[0];
let min = arr[0];

for (i = 0; i < n; i++) {
  if (max < arr[i]) {
    max = arr[i];
  }
  if (min > arr[i]) {
    min = arr[i];
  }
}

console.log(`${min} ${max}`);
