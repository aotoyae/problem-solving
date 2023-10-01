const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

for (i = 0; i < input.length - 1; i++) {
  let num = Number(input[i]);
  let numArr = [];
  let index = 1;
  let numAll = 0;

  while (index < num) {
    if (num % index === 0) numArr.push(index);
    index++;
    numAll = numArr.reduce((a, b) => a + b);
  }
  const str = numArr.join(" + ");
  if (num === numAll) {
    console.log(`${num} = ${str}`);
  } else {
    console.log(`${num} is NOT perfect.`);
  }
}
