function solution(id_pw, db) {
  const [id, pw] = id_pw;
  for (i = 0; i < db.length; i++) {
    if (db[i][0] === id && db[i][1] === pw) return "login";
    if (db[i][0] === id && db[i][1] !== pw) return "wrong pw";
  }
  return "fail";
}
