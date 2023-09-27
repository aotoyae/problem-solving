const fs = require("fs");
const input = fs.readFileSync(0, "utf8").split("\n");

const a = parseInt(input[0]);
const b = parseInt(input[1]);

const oneNum = b % 10;
const tenNum = Math.floor((b % 100) / 10);
const hundredNum = Math.floor(b / 100);

console.log(a * oneNum);
console.log(a * tenNum);
console.log(a * hundredNum);
console.log(a * b);
