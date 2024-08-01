function solution(my_string) {
  let result = 0;

  for (let item of my_string) {
    if (!isNaN(item)) result += Number(item);
  }

  return result;
}
