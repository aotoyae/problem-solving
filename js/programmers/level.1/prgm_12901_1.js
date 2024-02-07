function solution(a, b) {
  const week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  const lastDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  let day = b + 4;

  for (let i = 1; i < a; i++) {
    day += lastDays[i - 1];
  }

  return week[day % 7];
}
