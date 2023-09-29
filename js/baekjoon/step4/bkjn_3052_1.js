const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const newInput = input.map((x) => x % 42);
const set = new Set(newInput);
const uniqueArr = [...set];

console.log(uniqueArr.length);
