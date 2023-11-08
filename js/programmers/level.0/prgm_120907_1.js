function solution(quiz) {
  let array = [];
  let result = [];
  for (i = 0; i < quiz.length; i++) {
    array.push(quiz[i].split(" "));
  }
  for (j = 0; j < array.length; j++) {
    if (array[j][1] === "+") {
      Number(array[j][0]) + Number(array[j][2]) === Number(array[j][4])
        ? result.push("O")
        : result.push("X");
    } else {
      Number(array[j][0]) - Number(array[j][2]) === Number(array[j][4])
        ? result.push("O")
        : result.push("X");
    }
  }
  return result;
}
