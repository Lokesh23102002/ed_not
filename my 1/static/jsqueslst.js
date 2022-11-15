function pogf(gd){
    fd=JSON.parse(document.getElementById('fd').textContent);
    var url="/guidee/"+fd+"/"+gd
    window.location.href=url;
}