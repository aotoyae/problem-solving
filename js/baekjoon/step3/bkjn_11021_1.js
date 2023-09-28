const input = require("fs").readFileSync("dev/stdin").toString().split("\n");

let a = Number(input[0]);
let answer = "";

for (i = 1; i <= a; i++) {
  let num = input[i].split(" ").map((item) => Number(item));
  answer += `Case #${i}: ${num[0] + num[1]}\n`;
}
console.log(answer);

// 아래와 같음
// let a = Number(input[0]);

// for (i = 1; i <= a; i++) {
//   let num = input[i].split(" ").map((item) => Number(item));
//   console.log(`Case #${i}: ${num[0] + num[1]}`);
// }
