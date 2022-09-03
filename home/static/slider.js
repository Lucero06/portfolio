

window.onload = function () {
    var slider = document.getElementById("slider");
    var total_slides= slider.childElementCount;
    var i = 0;

    function slide(i, total_slides){
        console.log('inicio');
        console.log(i);
        var limit = total_slides-1;
        var j = i+1;
        var trans =j*100;
        console.log(trans);
        slider = document.getElementById("slider");
        console.log(slider);
        if (i < limit){
        slider.animate(
            [
                {transform: 'translateX(-'+trans+'vw)' }
            ],
            {
                duration:1000
            }
        );
        }
        setTimeout(
            function(){
                time=0;
                if (i < limit){
                    slider.style.transform='translateX(-'+trans+'vw)';

                    i+=1;
                    time=3000;
                }
                else{
                    i=0;
                }
                setTimeout(
                    function(){
                        slide(i,total_slides);
                    }
                    ,time
                );
            }
            ,1000
        );
    }

    slide(i,total_slides);
}; 