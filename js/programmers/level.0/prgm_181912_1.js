function solution(intStrs, k, s, l) {
  let result = [];
  for (a of intStrs) {
    result.push(Number(a.split("").splice(s, l).join("")));
  }
  return result.filter((a) => a > k);
}
