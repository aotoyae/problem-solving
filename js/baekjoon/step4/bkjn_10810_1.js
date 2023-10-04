const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
let baskets = Array(n);

for (i = 1; i <= m; i++) {
  let [start, end, ball] = input[i].split(" ").map(Number);
  for (j = start; j <= end; j++) {
    baskets[j - 1] = ball;
  }
}
for (k = 0; k < baskets.length; k++) {
  typeof baskets[k] === "undefined" ? (baskets[k] = 0) : baskets[k];
}

console.log(baskets.join(" "));
