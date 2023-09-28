const input = require("fs").readFileSync("dev/stdin").toString().split("\n");

let a = parseInt(input[0].split(" ")[0]);
let b = parseInt(input[0].split(" ")[1]);
let c = parseInt(input[0].split(" ")[2]);

if (a === b && b === c) {
  console.log(10000 + a * 1000);
} else if (a === b || b === c) {
  console.log(1000 + b * 100);
} else if (a === c) {
  console.log(1000 + a * 100);
} else {
  if (a > b && a > c) {
    console.log(a * 100);
  } else if (b > a && b > c) {
    console.log(b * 100);
  } else {
    console.log(c * 100);
  }
}
