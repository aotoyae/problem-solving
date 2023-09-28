const input = require("fs").readFileSync("dev/stdin").toString();

let n = Number(input);
let answer = "";

for (i = 1; i <= n / 4; i++) {
  answer += "long ";
}
console.log(`${answer}int`);
