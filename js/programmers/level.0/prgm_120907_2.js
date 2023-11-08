function solution(quiz) {
  let result = [];
  quiz.forEach((val) => {
    const [x, operator, y, equal, z] = val.split(" ");
    let sum = 0;
    if (operator === "+") {
      sum = Number(x) + Number(y);
    } else {
      sum = Number(x) - Number(y);
    }
    sum === Number(z) ? result.push("O") : result.push("X");
  });
  return result;
}
