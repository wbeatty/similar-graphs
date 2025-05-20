let myChart = null;

async function showGraph() {
  try {
    const response = await fetch("/get_graph_data");
    const data = await response.json();

    const ctx = document.getElementById("myChart").getContext("2d");

    // Destroy existing chart if it exists
    if (myChart) {
      myChart.destroy();
    }

    myChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: data.Date,
        datasets: [
          {
            label: "AMZN Stock Price",
            data: data["AMZN Close"],
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            borderColor: "rgba(255, 99, 132, 1)",
            borderWidth: 2,
            fill: false,
            yAxisID: "y",
          },
          {
            label: "S&P 500 Index",
            data: data["SPX Close"],
            backgroundColor: "rgba(54, 162, 235, 0.2)",
            borderColor: "rgba(54, 162, 235, 1)",
            borderWidth: 2,
            fill: false,
            yAxisID: "y1",
          },
        ],
      },
      options: {
        responsive: true,
        interaction: {
          mode: "index",
          intersect: false,
        },
        stacked: false,
        scales: {
          x: {
            title: {
              display: true,
              text: "Date",
            },
          },
          y: {
            type: "linear",
            display: true,
            position: "left",
            beginAtZero: false,
            title: {
              display: true,
              text: "AMZN Stock Price ($)",
            },
          },
          y1: {
            type: "linear",
            display: true,
            position: "right",
            beginAtZero: false,
            title: {
              display: true,
              text: "S&P 500 Index",
            },
            grid: {
              drawOnChartArea: false,
            },
          },
        },
        plugins: {
          tooltip: {
            callbacks: {
              label: function (context) {
                const label = context.dataset.label;
                const value = context.parsed.y;
                if (label.includes("AMZN")) {
                  return `${label}: $${value.toLocaleString(undefined, {
                    minimumFractionDigits: 2,
                    maximumFractionDigits: 2,
                  })}`;
                } else {
                  return `${label}: ${value.toLocaleString(undefined, {
                    minimumFractionDigits: 2,
                    maximumFractionDigits: 2,
                  })}`;
                }
              },
            },
          },
        },
      },
    });
  } catch (error) {
    console.error("Error fetching or displaying graph data:", error);
  }
}
