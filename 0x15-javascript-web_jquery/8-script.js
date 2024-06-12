$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: function (data) {
    const titleNum = data.results.length;
    const counter = 0;
    for (counter = 0; counter < titleNum; counter++) {
      const title = data.results[counter].title;
      $('UL#list_movies').append('<li>' + title + '</li>');
    }
  }
});
