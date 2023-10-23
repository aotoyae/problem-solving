function solution(my_string) {
  const result = Array(52).fill(0);
  for (i = 0; i < my_string.length; i++) {
    let code = my_string.charCodeAt(i);
    if (code >= 65 && code <= 90) {
      result[code - 65]++;
    } else {
      result[code - 71]++;
    }
  }
  return result;
}
