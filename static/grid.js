
function grid(){
    let grid = document.getElementById("grid-preview");
    var imgs=grid.children;
    console.log(imgs);
    var total_h=0;
    for (img of imgs){
        img.style.opacity=1;
        console.log(img.offsetWidth
            ,
            img.offsetHeight
            );
            total_h+=img.offsetHeight;
    }
    var height_column=total_h/1.9;
    console.log(height_column);
    grid.style.height=height_column;
}