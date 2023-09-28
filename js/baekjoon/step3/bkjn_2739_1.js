const input = require("fs").readFileSync("dev/stdin").toString();

let n = parseInt(input);
let i = 1;

while (i < 10) {
  console.log(`${n} * ${i} = ${n * i}`);
  i++;
}
