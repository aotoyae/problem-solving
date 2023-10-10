function solution(array, hight) {
  let answer = 0;
  for (i = 0; i < array.length; i++) {
    if (array[i] > hight) {
      answer++;
    }
  }
  return answer;
}
