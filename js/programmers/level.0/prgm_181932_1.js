function solution(code) {
  let codeCopy = [...code];
  let result = "";
  let mode = 0;

  for (i = 0; i < code.length; i++) {
    if (mode === 0) {
      if (codeCopy[i] !== "1") {
        if (i % 2 === 0) result += codeCopy[i];
      } else {
        mode = 1;
      }
    } else {
      if (codeCopy[i] !== "1") {
        if (i % 2 === 1) result += codeCopy[i];
      } else {
        mode = 0;
      }
    }
  }

  return result ? result : "EMPTY";
}
