function solution(my_string, queries) {
  let array = [...my_string];
  let result = "";
  for (i of queries) {
    let num = i[1] - i[0];
    result = array.slice(i[0], i[1] + 1).reverse();
    array.splice(i[0], num + 1);
    array.splice(i[0], 0, ...result);
  }
  return array.join("");
}
