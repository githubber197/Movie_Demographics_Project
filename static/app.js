let genresChartInstance = null;
let countriesChartInstance = null;
let ratingsChartInstance = null;
let heatmapChartInstance = null;

function fetchGenres() {
  const ageGroup = document.getElementById("ageGroupSelect").value;
  fetch(`http://localhost:8000/genres-by-age-group?age_group=${ageGroup}`)
    .then((response) => response.json())
    .then((data) => {
      if (genresChartInstance) genresChartInstance.destroy();
      const ctx = document.getElementById("ageChart").getContext("2d");
      genresChartInstance = new Chart(ctx, {
        type: "bar",
        data: {
          labels: data.map((d) => d.genre),
          datasets: [
            {
              label: "Count",
              data: data.map((d) => d.count),
              backgroundColor: "#D4922A",
              borderRadius: 4,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: false,
            },
          },
          scales: {
            y: { grid: { color: "#2a2a2a" } },
            x: { grid: { color: false } },
          },
        },
      });
    });
}
function fetchCountries() {
  const genre = document.getElementById("genreSelect").value;
  fetch(`http://localhost:8000/countries-by-genre?genre=${genre}`)
    .then((response) => response.json())
    .then((data) => {
      if (countriesChartInstance) countriesChartInstance.destroy();
      const ctx = document.getElementById("genresChart").getContext("2d");
      countriesChartInstance = new Chart(ctx, {
        type: "bar",
        data: {
          labels: data.map((d) => d.country),
          datasets: [
            {
              label: "Count",
              data: data.map((d) => d.count),
              backgroundColor: "#D4922A",
              borderRadius: 4,
            },
          ],
        },
        options: {
          indexAxis: "y",
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: false,
            },
          },
          scales: {
            y: { grid: { color: "#2a2a2a" } },
            x: { grid: { color: false } },
          },
        },
      });
    });
}
function fetchRatings() {
  fetch(`http://localhost:8000/avg-rating-by-age-group`)
    .then((response) => response.json())
    .then((data) => {
      if (ratingsChartInstance) ratingsChartInstance.destroy();
      const ctx = document.getElementById("ratingsChart").getContext("2d");
      ratingsChartInstance = new Chart(ctx, {
        type: "bar",
        data: {
          labels: data.map((d) => d.age_group),
          datasets: [
            {
              label: "Average Rating",
              data: data.map((d) => d.average_rating),
              backgroundColor: "#D4922A",
              borderRadius: 4,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: false,
            },
          },
          scales: {
            y: { grid: { color: "#2a2a2a" } },
            x: { grid: { color: false } },
          },
        },
      });
    });
}
function fetchStats() {
  fetch("http://localhost:8000/stats")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("totalMovies").textContent =
        data.total_movies.toLocaleString();
      document.getElementById("totalUsers").textContent =
        data.total_users.toLocaleString();
      document.getElementById("totalReviews").textContent =
        data.total_reviews.toLocaleString();
    });
}

function fetchTopMoviesByGenre() {
  const genre = document.getElementById("topGenreSelect").value;
  fetch(`http://localhost:8000/top-movies-by-genre?genre=${genre}`)
    .then((response) => response.json())
    .then((data) => {
      const tableBody = document.getElementById("topMoviesTableBody");
      tableBody.innerHTML = "";
      data.forEach((movie) => {
        const row = document.createElement("tr");
        row.innerHTML = `
          <td>${movie.movie_title}</td>
          <td>${movie.average_rating.toFixed(2)}</td>
        `;
        tableBody.appendChild(row);
      });
    });
}

function fetchMostReviewedMovies() {
  fetch(`http://localhost:8000/most-reviewed-movies`)
    .then((response) => response.json())
    .then((data) => {
      const tableBody = document.getElementById("mostReviewedTableBody");
      tableBody.innerHTML = "";
      data.forEach((movie) => {
        const row = document.createElement("tr");
        row.innerHTML = `
          <td>${movie.movie_title}</td>
          <td>${movie.review_count}</td>
        `;
        tableBody.appendChild(row);
      });
    });
}

function fetchHeatmap() {
  fetch("http://localhost:8000/genre-age-heatmap")
    .then((response) => response.json())
    .then((data) => {
      if (heatmapChartInstance) heatmapChartInstance.destroy();

      const ageGroups = [...new Set(data.map((d) => d.age_group))];
      const genres = [...new Set(data.map((d) => d.genre))];

      const matrixData = data.map((d) => ({
        x: d.genre,
        y: d.age_group,
        v: parseFloat(d.average_rating),
      }));

      const ctx = document.getElementById("heatmapChart").getContext("2d");
      heatmapChartInstance = new Chart(ctx, {
        type: "matrix",
        data: {
          datasets: [
            {
              label: "Avg Rating",
              data: matrixData,
              backgroundColor(context) {
                const value = context.dataset.data[context.dataIndex]?.v;
                const alpha = value ? (value - 3.5) / 1 : 0;
                return `rgba(212, 146, 42, ${Math.max(0.1, Math.min(1, alpha))})`;
              },
              width: ({ chart }) =>
                (chart.chartArea?.width || 0) / genres.length - 2,
              height: ({ chart }) =>
                (chart.chartArea?.height || 0) / ageGroups.length - 2,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            x: {
              type: "category",
              labels: genres,
              grid: { display: false },
              ticks: { color: "#666" },
            },
            y: {
              type: "category",
              labels: ageGroups,
              grid: { display: false },
              ticks: { color: "#666" },
            },
          },
        },
      });
    });
}
document.addEventListener("DOMContentLoaded", function () {
  fetchStats();
  fetchGenres();
  fetchCountries();
  fetchRatings();
  fetchMostReviewedMovies();
  fetchTopMoviesByGenre();
  fetchHeatmap();
});
