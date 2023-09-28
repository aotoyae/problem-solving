const input = require("fs").readFileSync("dev/stdin").toString();

let a = Number(input);
let result = "";

for (i = 1; i <= a; i++) {
  for (j = a - 1; j >= 0; j--) {
    result += j < i ? "*" : " ";
  }
  console.log(result);
}
