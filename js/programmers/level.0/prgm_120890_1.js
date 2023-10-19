function solution(array, n) {
  let array2 = [];
  let array3 = [];
  for (i in array) {
    array2.push(Math.abs(array[i] - n));
  }
  for (j = 0; j < array2.length; j++) {
    if (array2[j] === Math.min(...array2)) {
      array3.push(array[j]);
    }
  }
  return Math.min(...array3);
}
