// quiz validation
var checkedradio = false;

function radiovalidate(stepnumber)
{
    var checkradio = $("#step"+stepnumber+" input").map(function()
    {
    if($(this).is(':checked'))
    {
        return true;
    }
    else
    {
        return false;
    }
    }).get();

    checkedradio = checkradio.some(Boolean);
}



$(document).ready(function()
{
  setTimeout(function()
  {
    $(".input-field").each(function()
    {
      $(this).addClass('revealfield');
    })
  }, 1000)

})

$('.join').on('click', function()
{
    $('.signup').css('display', 'block');
    $('.login').css('display', 'none' );
})
$('.create').on('click', function()
{
    $('.signup').css('display', 'none');
    $('.login').css('display', 'block' );
})








// disable on enter
$('form').on('keyup keypress', function(e) {
    var keyCode = e.keyCode || e.which;
    if (keyCode === 13) { 
      e.preventDefault();
      return false;
    }
  });
  
  



// form validiation
$(document).ready(function()
   {

        $('#login').on('click', function()
        {
            $("#sub").html("<img src='assets/images/loading.gif'>");

                            
            var dataString = new FormData(document.getElementById("loginform"));


            // console.log(dataString);
            
            // send form to send.php
            $.ajax({
                        type: "POST",
                    url: "form handling/send.php",
                    data: dataString,
                        processData: false,
                        contentType: false,
                        success: function(data,status)
                        {

                        $("#sub").html("Success!");
                        
                        window.location = 'thankyou.html';
                        
                        },
                        error: function(data, status)
                        {
                        $("#sub").html("<span>failed!</span>");
                        }
                    });
        })
        $('#signup').on('click', function()
        {
            $("#sub").html("<img src='assets/images/loading.gif'>");

                            
            var dataString = new FormData(document.getElementById("signupform"));


            // console.log(dataString);
            
            // send form to send.php
            $.ajax({
                        type: "POST",
                    url: "form handling/send.php",
                    data: dataString,
                        processData: false,
                        contentType: false,
                        success: function(data,status)
                        {

                        $("#sub").html("Success!");
                        
                        window.location = 'thankyou.html';
                        
                        },
                        error: function(data, status)
                        {
                        $("#sub").html("<span>failed!</span>");
                        }
                    });
        })
   });












