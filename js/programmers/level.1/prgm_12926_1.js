function solution(s, n) {
  let answer = "";

  for (let i = 0; i < s.length; i++) {
    if (s[i] === " ") {
      answer += " ";
    } else {
      let code = s.charCodeAt(i);
      if (code <= 90) {
        code += n;
        if (code > 90) code -= 26;
      } else {
        code += n;
        if (code > 122) code -= 26;
      }
      answer += String.fromCharCode(code);
    }
  }

  return answer;
}
