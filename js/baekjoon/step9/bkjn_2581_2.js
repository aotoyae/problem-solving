const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let M = Number(input[0]);
let N = Number(input[1]);

const array = Array(N - M + 1)
  .fill()
  .map((_, index) => M + index);
console.log(array);

const answer = array.filter((num) => {
  for (let i = 2; num > i; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return num > 1;
});

if (answer.length) {
  console.log(answer.reduce((a, b) => (a += b))); //+=?
  console.log(answer[0]);
} else {
  console.log(-1);
}
