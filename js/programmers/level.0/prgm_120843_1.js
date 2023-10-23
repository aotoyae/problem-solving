function solution(numbers, k) {
  let ball = 1;
  for (i = 1; i < k; i++) {
    ball += 2;
    if (ball > numbers.length) {
      ball -= numbers.length;
    }
  }
  return ball;
}
