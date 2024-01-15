function solution(numbers) {
  let newNum = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  let totalNewNum = newNum.reduce((a, b) => a + b);
  let totalNumbers = numbers.reduce((a, b) => a + b);

  return totalNewNum - totalNumbers;
}
