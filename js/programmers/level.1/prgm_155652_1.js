function solution(s, skip, index) {
  let answer = '';

  for (const i of s) {
    let code = i.charCodeAt();

    for (let j = 0; j < index; j++) {
      code += 1;
      if (code > 122) code = 97;

      while (skip.includes(String.fromCharCode(code))) {
        code += 1;
        if (code > 122) code = 97;
      }
    }

    answer += String.fromCharCode(code);
  }

  return answer;
}
