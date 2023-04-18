const labels = ["1월", "2월", "3월", "4월", "5월", "6월", "7월"];
const data = {
    labels: labels,
    datasets: [
        {
            label: "1",
            data: [65, 59, 80, 81, 56, 55, 40],
            fill: false,
            borderColor: "rgb(0,255,127)",
            tension: 0.1,
        },
        {
            label: "2",
            data: [50, 29, 40, 21, 46, 25, 30],
            fill: false,
            borderColor: "rgb(0,100,0)",
            tension: 0.1,
        },
    ],
};
// </block:setup>

// <block:config:0>
const config = {
    type: "line",
    data: data,
};
// </block:config>

const ctx = document.getElementById("lineChart").getContext("2d");
const myChart = new Chart(ctx, config);
