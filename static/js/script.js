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

    const names = Object.keys(data).filter((key) => key !== "Date");

    myChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: data.Date,
        datasets: [
          {
            label: names[0],
            data: data[names[0]],
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            borderColor: "rgba(255, 99, 132, 1)",
            borderWidth: 2,
            fill: false,
            yAxisID: "y",
          },
          {
            label: names[1],
            data: data[names[1]],
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
              text: names[0],
            },
          },
          y1: {
            type: "linear",
            display: true,
            position: "right",
            beginAtZero: false,
            title: {
              display: true,
              text: names[1],
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
                if (label.includes(names[0])) {
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
