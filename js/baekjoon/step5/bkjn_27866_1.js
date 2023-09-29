const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const word = input[0].toString();
const num = Number(input[1]);

console.log(word[num - 1]);
