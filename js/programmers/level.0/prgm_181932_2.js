function solution(code) {
  let result = "";
  let mode = 0;

  for (i = 0; i < code.length; i++) {
    if (Number(code[i]) === 1) {
      mode = mode === 0 ? 1 : 0;
    }
    if (Number(code[i]) !== 1 && i % 2 === mode) {
      result += code[i];
    }
  }

  return result ? result : "EMPTY";
}
