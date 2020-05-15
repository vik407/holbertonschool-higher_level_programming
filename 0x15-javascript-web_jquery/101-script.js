// Write a Javascript script that adds, removes and clears LI elements from a list when the user clicks
$(document).ready(() => {
  // add
  $('#add_item').click(() => {
    $('.my_list').append('<li>Item</li>');
  });
  // remove last
  $('#remove_item').click(() => {
    $('.my_list li:last-child').remove();
  });
  // remove all
  $('#clear_list').click(() => {
    $('.my_list').find('li').remove();
  });
});
