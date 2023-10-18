function solution(my_string) {
  return my_string
    .split(/\d+/)
    .map(Number)
    .reduce((a, b) => a + b);
}
