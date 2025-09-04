function translateText() {
  const inputText = document.getElementById("input-text").value;
  if (inputText != "") {
    axios
      // 翻訳処理をお願いする
      .get("/translate" + "?input_text=" + inputText)

      // しばらくすると、取得したテキストがresponseに格納される
      .then((response) => {
        const textbox = document.getElementById("output-text");
        textbox.innerText = response.data;
      });
  }
}
