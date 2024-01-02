function solution(s) {
  let str = s.toUpperCase();
  let pCount = 0;
  let yCount = 0;

  for (let i of str) {
    if (i === "P") {
      pCount++;
    } else if (i === "Y") {
      yCount++;
    }
  }
  return pCount === yCount ? true : false;
}
