function solution(s) {
  let rule = /^\d{6}$|^\d{4}$/;
  return rule.test(s);
}
