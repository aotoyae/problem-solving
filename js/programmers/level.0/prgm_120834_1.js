function solution(age) {
  const arr = age.toString().split("");
  const alphabet = "abcdefghij";
  return arr.map((a) => alphabet[a]).join("");
}
