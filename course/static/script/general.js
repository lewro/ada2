$(document).ready(function(){
  // Top Messages
  $('.top-messages').delay(3500).fadeOut();
});

$(document).ready(function(){
  // Init select drop downs
  $('select').formSelect();

  // Tabs
  $(document).ready(function(){
    $('.tabs').tabs();
  });

  $('label').click(function() {
    $(this).prev('input').focus().click();
    $(this).prev('textarea').focus().click();
  });

  // Footer Form
  $('.close-fm').click(function() {
    $('.footer-form').hide(250, function() {
      $('.footer-form-btn').show();
    });
  });

  $('.footer-form-btn').click(function() {
    $('.footer-form').show(250);
    $(this).hide()
  });

  $('#contact-form').on('submit', function(e) {
     return validateForm(this);
  });

  // Modules - Lessons
  $('.module').click(function() {
    $('.module').removeClass('active');
    $(this).addClass('active');

    var target = $(this);

    $([document.documentElement, document.body]).animate({
      scrollTop: $(target).offset().top
    }, 500);

    return false;
  });
});


