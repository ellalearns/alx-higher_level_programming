document.addEventListener('DOMContentLoaded', () => {
  const newElem = '<li>Item</li>';
  const domToMod = 'UL.my_list';

  $('DIV#add_item').on('click', function () {
    $(domToMod).append(newElem);
  });

  $('DIV#remove_item').on('click', function () {
    $(domToMod).children(':last-child').remove();
  });

  $('DIV#clear_list').on('click', function () {
    $(domToMod).empty();
  });
});
