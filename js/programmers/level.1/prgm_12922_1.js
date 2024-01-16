function solution(n) {
  let str = "";

  if (n % 2 === 0) {
    for (let i = 1; i <= n / 2; i++) {
      str += "수박";
    }
  } else {
    for (let i = 1; i <= Math.floor(n / 2); i++) {
      str += "수박";
    }
    str += "수";
  }

  return str;
}
