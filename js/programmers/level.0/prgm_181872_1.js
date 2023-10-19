function solution(myString, pat) {
  let num = 0;
  if (pat.length > 1) {
    num += myString.lastIndexOf(pat) + pat.length - 1;
    return myString.slice(0, num + 1);
  } else {
    num += myString.lastIndexOf(pat);
    return myString.slice(0, num + 1);
  }

  // return myString.slice(0, myString.lastIndexOf(pat) + pat.length);
}
