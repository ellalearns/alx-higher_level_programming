$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: function (data) {
    const results = data.results;
    $.each(results, function (i) {
      $('UL#list_movies').append('<li>' + results[i].title + '</li>');
    });
  }
});
