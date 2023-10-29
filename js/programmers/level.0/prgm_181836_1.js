function solution(picture, k) {
  let result = [];
  picture.forEach((v) => {
    const repeat = [...v].map((v) => v.repeat(k)).join("");
    for (i = 0; i < k; i++) {
      result.push(repeat);
    }
  });
  return result;
}
