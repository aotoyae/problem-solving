const input = require("fs").readFileSync("dev/stdin").toString().trim();

const result = [];

for (i = 97; i <= 122; i++) {
  result.push(input.indexOf(String.fromCharCode(i)));
}
console.log(result.join(" "));
