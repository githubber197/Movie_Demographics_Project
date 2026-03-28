let genresChartInstance = null;
let countriesChartInstance = null;
let ratingsChartInstance = null;

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
document.addEventListener("DOMContentLoaded", function() {
    fetchStats();
    fetchGenres();
    fetchCountries();
    fetchRatings();
});