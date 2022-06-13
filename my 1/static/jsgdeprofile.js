window.alert("came");
function chat(){
    window.alert("came");
    gde=JSON.parse(document.getElementById('gde').textContent);
    ques_id=JSON.parse(document.getElementById('ques_id').textContent);
    fd_no=JSON.parse(document.getElementById('fd_no').textContent);
    url="/chat/"+ gde+"?requestfrom=guide&fd_no="+fd_no+"&ques_id="+ques_id;
    window.alert("came");
    window.location.href=url;
}

function shrevs(){
    document.getElementById("rvs").style.display= 'grid';
}
