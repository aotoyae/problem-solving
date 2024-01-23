function solution(s) {
  arr = s.split(" ");
  answer = "";

  for (let word of arr) {
    for (let i = 0; i < word.length; i++) {
      i % 2
        ? (answer += word[i].toLowerCase())
        : (answer += word[i].toUpperCase());
    }
    answer += " ";
  }

  return answer.slice(0, -1);
}
