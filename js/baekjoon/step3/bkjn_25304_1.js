const input = require("fs").readFileSync("dev/stdin").toString().split("\n");

let x = Number(input[0]);
// === let x = +input[0]
let n = Number(input[1]);
let total = 0;

for (i = 2; i <= n + 1; i++) {
  let price = input[i].split(" ").map((item) => Number(item));
  total += price[0] * price[1];
}
// for (i = 2; i <= n + 1; i++) {
//   let price = input[i].split(" ");
//   total += Number(price[0]) * Number(price[1]);
// }

console.log(x === total ? "Yes" : "No");
