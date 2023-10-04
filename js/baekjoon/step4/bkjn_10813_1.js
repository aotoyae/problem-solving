const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
let baskets = [];

for (i = 0; i < n; i++) {
  baskets.push(i + 1);
}

for (j = 1; j <= m; j++) {
  let [a, b] = input[j].split(" ").map(Number);
  let tmp = baskets[a - 1];
  baskets[a - 1] = baskets[b - 1];
  baskets[b - 1] = tmp;
}
console.log(baskets.join(" "));
