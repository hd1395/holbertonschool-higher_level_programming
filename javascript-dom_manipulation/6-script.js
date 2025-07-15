#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
fetch(url)
  .then(response => {
    if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }
  return response.json();
  })
  .then(data => {
    const characterName = data.name;
    document.querySelector("#character").textContent = characterName;
  })
