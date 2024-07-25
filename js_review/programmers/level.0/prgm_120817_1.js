function solution(numbers) {
  const answer = numbers.reduce((a, b) => {
    return a + b;
  }, 0);

  return answer / numbers.length;
}
