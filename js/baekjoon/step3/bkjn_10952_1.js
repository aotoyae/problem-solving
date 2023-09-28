const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

for (i = 0; i <= input.length; i++) {
  let num = input[i].split(" ").map((item) => Number(item));
  answer = num[0] + num[1];

  if (answer === 0) {
    break;
  } else {
    console.log(answer);
  }
}

// for (i = 0; i < input.length-1; i++) {
//   let num = input[i].split(" ").map((item) => Number(item));
//   console.log(num[0] + num[1]);
// }
