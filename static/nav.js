     function nav_img(){
        // nav img
        var active= document.getElementsByClassName("active-nav")[0];
        var rect = active.getBoundingClientRect();
        var docEl = document.documentElement;
        var left = rect.left + (window.pageXOffset || docEl.scrollLeft || 0);
        var img = document.getElementById("img-nav");
        if(img){
         var width_img = img.offsetWidth;
        var width_link = active.offsetWidth;
        var diff = width_img-width_link;
        var diff_apply=diff/2;
        var apply = left - diff_apply;
        img.style.left=apply+"px";
        img.style.opacity="1";
        }
        
     }
     