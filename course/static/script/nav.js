$(document).ready(function(){

  function closeAll() {
    $('#navigation ul').hide();
    $('#navigation li, #navigation h2').removeClass('active');
  }

  $('#navigation h2').click(function(){
    closeAll();
    $(this).next('ul').show();
    $(this).addClass('active');
  });

  $('#close-sidebar').click(function(){
    $('body').addClass('hide-nav');
    $('#sidebar').hide();
    $('#show-sidebar').show();
    $(this).hide();
  });

  $('#show-sidebar').click(function(){
    $('body').removeClass('hide-nav');
    $('#sidebar').show();
    $("#close-sidebar").show();
    $(this).hide();
  });

});
