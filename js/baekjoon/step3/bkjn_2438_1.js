const input = require("fs").readFileSync("dev/stdin").toString();

let a = Number(input);
let result = "";

for (i = 1; i <= a; i++) {
  result += "*";
  console.log(result);
}
