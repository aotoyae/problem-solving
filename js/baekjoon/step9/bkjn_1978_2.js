const { chmod } = require("fs");

const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let nums = input[1].split(" ").map((item) => item * 1);
let answer = 0;
for (i = 0; i < nums.length; i++) {
  if (nums[i] !== 1) {
    let count = 0;
    for (j = 2; j < nums[i]; j++) {
      if (nums[i] % j === 0) {
        count++;
      }
    }
    if (count === 0) {
      answer++;
    }
  }
}
console.log(answer);
