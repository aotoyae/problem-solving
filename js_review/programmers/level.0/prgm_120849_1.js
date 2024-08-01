function solution(my_string) {
  const words = ['a', 'e', 'i', 'o', 'u'];

  words.forEach((word) => (my_string = my_string.replaceAll(word, '')));

  return my_string;
}
