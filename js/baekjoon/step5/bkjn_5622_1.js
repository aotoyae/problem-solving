const input = require("fs").readFileSync("dev/stdin").toString().trim();

let code = {
  2: "ABC",
  3: "DEF",
  4: "GHI",
  5: "JKL",
  6: "MNO",
  7: "PQRS",
  8: "TUV",
  9: "WXYZ",
};
let result = 0;

for (i = 0; i < input.length; i++) {
  for (j = 2; j <= 9; j++) {
    if (code[j].includes(input[i])) {
      result += j + 1;
      break;
    }
  }
}
console.log(result);
