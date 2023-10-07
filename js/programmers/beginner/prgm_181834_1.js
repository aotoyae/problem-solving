function solution(myString) {
  myString.split("");
  let answer = [];
  for (i = 0; i < myString.length; i++) {
    if (myString[i].charCodeAt() <= 107) {
      answer.push("l");
    } else {
      answer.push(myString[i]);
    }
  }
  return answer.join("");
  // 한 줄로 가능
  // return myString.replace(/[a-k]/g,'l')
  // 알파벳도 크기 비교 가능
  // return [...myString].map((v) => v < 'l' ? 'l' : v).join('');
}
