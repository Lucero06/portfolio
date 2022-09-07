

window.onload = function () {


    var active= document.getElementsByClassName("active-nav")[0];
    var rect = active.getBoundingClientRect();
    var docEl = document.documentElement;
    var left = rect.left + (window.pageXOffset || docEl.scrollLeft || 0);
    var img = document.getElementById("img-nav");
    var width_img = img.offsetWidth;
    var width_link = active.offsetWidth;
    var diff = width_img-width_link;
    var diff_apply=diff/2;
    var apply = left - diff_apply;
    img.style.left=apply+"px";
    img.style.visibility="initial";

    //slider
    var slider = document.getElementById("slider");
    var total_slides= slider.childElementCount;
    var i = 0;

    function slide(i, total_slides){
        //console.log('inicio');
        //console.log(i);
        var limit = total_slides-1;
        var j = i;
        var trans =j*100;
        //console.log(trans);
        slider = document.getElementById("slider");
        //console.log(slider);
        if ( i > 0){
            slider.style.opacity=".55";
            for (ele of slider.children){
                ele.children[0].animate(
                    [
                        {transform:'skew(-5deg, 0deg)'},
                        {transform:'skew(0deg, 0deg)'},
                    ],{
                        duration:1000,
                        easing:'ease'
                    }
                );
            }
        }
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
                slider.style.opacity="1";
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