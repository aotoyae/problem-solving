function solution(my_string, s, e) {
  const arr = [...my_string];
  const reverseArr = arr.slice(s, e + 1).reverse();
  arr.splice(s, reverseArr.length, ...reverseArr);
  return arr.join("");
}
