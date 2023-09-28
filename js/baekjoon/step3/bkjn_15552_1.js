const input = require("fs").readFileSync("dev/stdin").toString().split("\n");

let a = Number(input[0]);
let answer = "";

for (i = 1; i <= a; i++) {
  let num = input[i].split(" ").map((item) => Number(item));
  answer += num[0] + num[1] + "\n";
}
console.log(answer);
