const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
let baskets = Array(n)
  .fill()
  .map((v, i) => i + 1);

for (j = 1; j <= m; j++) {
  let [a, b] = input[j].split(" ").map(Number);
  let tmp = [];
  for (k = a - 1; k < b; k++) {
    tmp.push(baskets[k]);
  }
  tmp.reverse();
  baskets.splice(a - 1, b - a + 1, ...tmp);
}
console.log(baskets.join(" "));
