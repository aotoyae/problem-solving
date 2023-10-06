function solution(money) {
  const americano = 5500;
  const cup = Math.floor(money / americano);
  const change = money % americano;
  const answer = [cup, change];

  return answer;
}
