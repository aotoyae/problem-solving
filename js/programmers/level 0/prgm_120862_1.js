function solution(numbers) {
  numbers.sort((a, b) => b - a);
  let first = numbers[0] * numbers[1];
  let last = numbers[numbers.length - 1] * numbers[numbers.length - 2];
  return first > last ? first : last;

  // 오름차순 변경 후
  // return Math.max(numbers[0]*numbers[1], numbers[numbers.length-1]*numbers[numbers.length-2]);
}
