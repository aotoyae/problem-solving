const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let q = input[0].split(" ");
let a = Number(q[0].split("").reverse().join(""));
let b = Number(q[1].split("").reverse().join(""));

console.log(a > b ? a : b);
