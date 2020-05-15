// Write a Javascript script that fetches and lists all movies title by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', data => {
  data.results.forEach(mov => {
    $('#list_movies').append(`<li>${mov.title}</li>`);
  });
});
