function solution(numbers) {
  const num = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  num.forEach((a, i) => {
    numbers = numbers.split(a).join(i);
  });
  return Number(numbers);
}
