const maxWith1115 = () => {
    const sidebar = document.querySelector(".sidebar");
    const main = document.querySelector(".main");
    if (window.matchMedia("(max-width: 1115px)").matches) {
        // 만약 미디어 쿼리를 만족하면, `.sidebar`와 `.main` 요소의 스타일을 수정합니다.
        sidebar.style.width = "60px";
        main.style.left = "60px";
        main.style.width = "calc(100% - 60px)";
    }
};

const maxWith880 = () => {
    const cards = document.querySelector(".cards");
    const charts = document.querySelector(".charts");
    const chart = document.querySelector(".chart");

    if (window.matchMedia("(max-width: 880px)").matches) {
        cards.style.gridTemplateColumns = "repeat(2, 1fr)";
        charts.style.gridTemplateColumns = "1fr";
    }
};

const maxWith500 = () => {
    const topbar = document.querySelector(".topbar");
    const cards = document.querySelector(".cards");

    if (window.matchMedia("(max-width: 500px)").matches) {
        topbar.style.gridTemplateColumns = "1fr 5fr 0 0.4fr 1fr";
        cards.style.gridTemplateColumns = "1fr";
    }
};

const handleResizeEvenet = () => {
    maxWith1115();
    maxWith880();
    maxWith500();
};

maxWith1115();
maxWith880();
maxWith500();

window.addEventListener("resize", handleResizeEvenet);
