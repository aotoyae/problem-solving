const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let x = [];

for (i = 1; i < 31; i++) {
  if (input.includes(i)) continue;
  x.push(i);
}

x.sort((a, b) => a - b);
console.log(`${x[0]}\n${x[1]}`);
