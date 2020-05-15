// Write a Javascript script that fetches and replaces the name of this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', data => {
  $('#character').append(`<p>${data.name}</p>`);
});
