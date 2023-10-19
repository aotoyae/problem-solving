function solution(s) {
  let array = s.split(" ");
  while (array.includes("Z")) {
    const index = array.findIndex((a) => a === "Z");
    array.splice(index - 1, 2);
  }
  return array.reduce((a, b) => a + Number(b), 0);
}
