/*
index.js
 */

$(function (){
    $(window).on('scroll', function (){
        if($(document).scrollTop()>=$('#headerBox').height()){
            $('#mainMenuBox').addClass('mainMenuFixed');
        } else{
            $('#mainMenuBox').removeClass('mainMenuFixed');
        }
    });

    $(window).resize(function (){
        var width_size = window.innerWidth;

        if(width_size <= 800){
            $('#inputBox input').css({"display": "none"});
            $('#topMenuBox').css({"display": "none"});
            $('#logoBox').css({"left":"50%"})
        } else if (width_size <=1250){
           $('#inputBox input').css({"display": "none"});
           $('#inputBox button').css({"border-left": "none"});
        } else if (width_size >= 1250){
            $('#topMenuBox').css({"display" : "inline-block"});
            $('#inputBox input').css({"display" : "inline-block"});
            $('#inputBox button').css({"border-left": "solid 1px gray"});
            $('#logoBox').css({"left":"0"})
        }
    });
});