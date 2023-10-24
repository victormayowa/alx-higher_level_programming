const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const filmsData = JSON.parse(body);
    const filmsWithWedgeAntilles = filmsData.results.filter(film =>
      film.characters.includes("https://swapi-api.alx-tools.com/api/people/18/")
    );
    console.log(filmsWithWedgeAntilles.length);
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
