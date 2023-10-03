const { chmod } = require("fs");

const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let nums = input[1].split(" ");

for (i = 0; i < nums.length; i++) {
  let numArr = [];
  let number = Number(nums[i]);
  let index = 1;
  let primeArr = [];
  let primeNum = 0;
  while (index <= number) {
    if (number % index === 0) numArr.push(index);
    index++;
  }
  if (numArr[0] === 1 && numArr[1] === number && numArr.length === 2) {
    primeNum += 1;
    console.log(primeNum);
  }
}
