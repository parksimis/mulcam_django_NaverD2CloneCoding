/*
slideShow.js
 */

$(function () {
    var movedIndex = 0;

    function moveSlide(index){
        movedIndex = index;

        var moveLeft = -(movedIndex * 1900);
        $('#slidePanel').animate({'left' : moveLeft}, 'slow');
        $('.controlButton').eq(movedIndex-1).css({"opacity" : "0.5"})
        $('.controlButton').eq(movedIndex).css({"opacity" : "1"})
    }

    $('#prevButton').on('click', function (){
        if(movedIndex != 0)
            movedIndex = movedIndex - 1;
        else if(movedIndex == 0){
            movedIndex = 3
        }
        moveSlide(movedIndex);
    });

    $('#nextButton').on('click', function (){
        if(movedIndex != 3)
            movedIndex = movedIndex + 1;
        else if(movedIndex == 3){
            movedIndex = 0;
        }

        moveSlide(movedIndex);
    });

    $('.controlGroup').each(function (index){
        $(this).on('click', function (){
            moveSlide(index);
        })
    });

});