function solution(numbers) {
  const answer = numbers.reduce((a, b) => a + b) / numbers.length;
  return answer;
}
