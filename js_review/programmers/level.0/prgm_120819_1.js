function solution(money) {
  const americano = 5500;
  const cups = ~~(money / americano);
  const change = money % americano;

  return [cups, change];
}
