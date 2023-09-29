const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let [n, m] = input[0].split(" ").map(Number);
let baskets = new Array(n).fill(0);

for (i = 0; i <= m; i++) {
  const [start, end, ball] = input[i].split(" ").map(Number);
  for (j = start; j <= end; j++) {
    baskets[j - 1] = ball;
  }
}
console.log(baskets.join(" "));
