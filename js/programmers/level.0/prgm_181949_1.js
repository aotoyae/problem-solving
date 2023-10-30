const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input = [line];
}).on("close", function () {
  str = input[0];
  let arr = [];
  for (i = 0; i < str.length; i++) {
    str[i] === str[i].toUpperCase()
      ? arr.push(str[i].toLowerCase())
      : arr.push(str[i].toUpperCase());
  }
  console.log(arr.join(""));
});
