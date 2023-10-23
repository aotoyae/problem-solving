function solution(my_string) {
  const array = my_string.split(" ");
  let answer = Number(array[0]);
  for (i = 1; i < array.length; i += 2) {
    array[i] === "+"
      ? (answer += Number(array[i + 1]))
      : (answer -= Number(array[i + 1]));
  }
  return answer;
}
