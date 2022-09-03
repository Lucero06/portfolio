

window.onload = function () {
    var slider = document.getElementById("slider");
    var total_slides= slider.childElementCount;
    var i = 0;

    function slide(i, total_slides){
        console.log('inicio');
        console.log(i);
        var limit = total_slides-1;
        var j = i;
        var trans =j*100;
        console.log(trans);
        slider = document.getElementById("slider");
        console.log(slider);
        slider.animate(
            [
                {transform: 'translateX(-'+trans+'vw)' }
            ],
            {
                duration:1000
            }
        );
        setTimeout(
            function(){
                time=3000;
                slider.style.transform='translateX(-'+trans+'vw)';
                if (i < limit){
                    i+=1;
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