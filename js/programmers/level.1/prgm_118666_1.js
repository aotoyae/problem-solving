function solution(survey, choices) {
  const mbti = { R: 0, T: 0, C: 0, F: 0, J: 0, M: 0, A: 0, N: 0 };
  const category = ['RT', 'CF', 'JM', 'AN'];

  for (let i = 0; i < choices.length; i++) {
    if (choices[i] < 4) mbti[survey[i][0]] += 4 - choices[i];
    else mbti[survey[i][1]] += choices[i] - 4;
  }

  return category.reduce(
    (a, b) => a + (mbti[b[0]] >= mbti[b[1]] ? b[0] : b[1]),
    ''
  );
}
