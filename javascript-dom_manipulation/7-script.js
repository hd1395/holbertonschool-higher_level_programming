#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
fetch(url)
  .then(response => {
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
    return response.json();
  })
  .then(data => {
    document.querySelector('#list_movies').innerHTML = '';

    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      document.querySelector('#list_movies').appendChild(li);
    });
  });
