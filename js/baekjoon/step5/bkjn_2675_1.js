const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let a = Number(input[0]);

for (i = 1; i <= a; i++) {
  let arr = input[i].split(" ");
  let str = arr[1];
  let strLength = arr[1].length;
  let answer = "";
  for (j = 0; j < strLength; j++) {
    answer += str[j].repeat(arr[0]);
  }
  console.log(answer);
}
