$(document).ready(() => {

  $('.add-to-favourite-btn').on('click', () => {
    $('.add-to-favourite-btn').hide()
    $('.delete-from-favourite-btn').show()
    alert("This recipe was added to 'Your favourites'");
  });

   $('.delete-from-favourite-btn').on('click', () => {
    $('.delete-from-favourite-btn').hide()
    $('.add-to-favourite-btn').show()
    alert("This recipe was deleted from 'Your favourites'");
  });


  $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });
});


//alert("This recipe was added to 'Favourites'");