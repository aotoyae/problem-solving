function solution(my_string, index_list) {
  let answer = [];
  for (i = 0; i < index_list.length; i++) {
    answer.push(my_string[index_list[i]]);
  }
  return answer.join("");
  // 한 줄로 가능
  // return index_list.map(i => my_string[i]).join('')
}
