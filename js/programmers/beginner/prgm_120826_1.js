function solution(my_string, letter) {
  const newArray = [];
  for (i = 0; i < my_string.length; i++) {
    if (my_string[i] === letter) {
      continue;
    } else {
      newArray.push(my_string[i]);
    }
  }
  return newArray.join("");
}
