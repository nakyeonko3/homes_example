console.log("hello, world");

async function getWaifuImgUrl() {
  const response = await fetch("https://api.waifu.pics/sfw/waifu");
  const message = await response.json();
  console.log("getWaifuImgUrl()");
  return message.url;
}

async function renderWaituImg() {
  const div = document.querySelector("#imghere");
  console.log("before");
  const url = await getWaifuImgUrl();
  console.log("after");

  const myImage = new Image(100, 100);
  myImage.src = url;
  div.appendChild(myImage);
}
renderWaituImg();
// getWaifuImgUrl();

// 패치 이미지 생성 변수명
