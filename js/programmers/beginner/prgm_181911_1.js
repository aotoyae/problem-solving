function solution(my_string, parts) {
  let answer = "";
  for (i = 0; i < my_string.length; i++) {
    answer += my_string[i].split("").slice(parts[i][0], parts[i][1] + 1);
  }
  return answer.join("");
}
