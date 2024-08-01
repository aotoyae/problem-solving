function solution(my_string) {
  const words = ['a', 'e', 'i', 'o', 'u'];

  for (let word of words) {
    my_string = my_string.replaceAll(word, '');
  }

  return my_string;
}
