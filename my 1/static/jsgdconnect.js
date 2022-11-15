function chat(){
    c_m=JSON.parse(document.getElementById('c_m').textContent);
    if (c_m=="1"){
        gd=JSON.parse(document.getElementById('gd').textContent);
        fd_no=JSON.parse(document.getElementById('fd_no').textContent);
        ques_id=JSON.parse(document.getElementById('ques_id').textContent);
        url="/chat/"+gd+"?requestfrom=guidee"+"&fd_no="+fd_no+"&ques_id="+ques_id;
        window.location.href=url;
    }
}