const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let num = input[0].split(" ");
let a = Number(num[0]);
let b = Number(num[1]);
let aArr = [];
let index = 1;

while (index <= a) {
  if (a % index === 0) aArr.push(index);
  index++;
}
if (aArr.length < b) {
  console.log(0);
} else {
  console.log(aArr[b - 1]);
}
