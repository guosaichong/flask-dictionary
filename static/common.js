function js_method(word){
    var str='<audio controls="" autoplay="" name="media" src="http://dict.youdao.com/dictvoice?audio='+word+'&amp;type=1" type="audio/mpeg"></audio>'
    var child=document.createElement("div");
    child.innerHTML=str;
}

