let context = $("#lineChart").get(0).getContext('2d');

let chartData = $('#data').data('chart_data')

let chart = new Chart(context, {
    type: 'line',
    data: {
        labels: chartData.labels,
        datasets: [
            {
                label: "registrations",
                data: chartData.registrationsCount,
                fill: false,
                lineTension: 0.2,
                backgroundColor: "#27ab4f"
            },
            {
                label: "orders",
                data: chartData.ordersCount,
                fill: false,
                lineTension: 0.2,
                backgroundColor: "#9fe817",
            },
        ]
    },
    options: {
        responsive: true
    },
})