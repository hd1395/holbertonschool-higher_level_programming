#!/usr/bin/node
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    document.querySelector('#hello').textContent = data.hello;
  });
