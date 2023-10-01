const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

for (i = 0; i < input.length - 1; i++) {
  let num = input[i].split(" ").map((item) => item * 1);
  let a = num[0];
  let b = num[1];
  if (b % a === 0) {
    console.log("factor");
  } else if (a % b === 0) {
    console.log("multiple");
  } else {
    console.log("neither");
  }
}
