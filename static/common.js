function js_method(word){
    var str='<audio controls="" autoplay="" name="media" src="http://dict.youdao.com/dictvoice?audio='+word+'&amp;type=1" type="audio/mpeg"></audio>'
    // var parent=document.getElementsByClassName("word");
    var child=document.createElement("div");
    child.id="child_div";
    child.innerHTML=str;
    child.remove();
}

