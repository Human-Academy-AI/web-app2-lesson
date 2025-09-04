function sendText() {
  // テキストボックスの中身を取り出す
  const inputText = document.getElementById("input-text").value;

  axios
    // テキストを送信 & 取得する
    .get("/send" + "?text=" + inputText)

    // しばらくすると、取得したテキストがresponseに格納される
    .then((response) => {
      // textboxというIDの要素にテキストを入れる
      document.getElementById("textbox").innerText = response.data;
    });
}
