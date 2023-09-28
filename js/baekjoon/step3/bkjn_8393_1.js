const input = require("fs").readFileSync("dev/stdin").toString();

let n = 0;
for (i = 1; i <= input; i++) {
  n += i;
}
console.log(n);
