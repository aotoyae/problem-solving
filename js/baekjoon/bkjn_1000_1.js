// const input = require("fs").readFileSync(0, 'utf8').split(" ");
// console.log(Number(input[0]) + Number(input[1]));

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").split(" ");

const a = parseInt(input[0]);
const b = parseInt(input[1]);

console.log(a + b);
