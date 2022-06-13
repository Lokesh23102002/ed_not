function sbmtqs() {
    var ques=document.getElementById('ques').value;
    var url=window.location.href;
    url=url.substring(0,url.length-9);
    url+="relatedqueslst";
    url+="?ques="+ques;
    window.location.href= url;
}