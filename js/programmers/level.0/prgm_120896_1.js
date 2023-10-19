function solution(s) {
  let result = [];
  let sArray = [...s];
  sArray.forEach((a) => {
    if (s.indexOf(a) === s.lastIndexOf(a)) {
      result.push(a);
    }
  });
  return result.sort().join("");
}
