function js_method(word){
    var str='<video controls="" autoplay="" name="media"><source src="http://dict.youdao.com/dictvoice?audio='+word+'&amp;type=1" type="audio/mpeg"></video>'
    // var parent=document.getElementsByClassName("word");
    var child=document.createElement("div");
    child.id="child_div";
    child.innerHTML=str;
    child.remove();
}
function checkValidate(){
    var onAccount=document.getElementById('account');
    var accountErr=document.getElementById("accountErr");
    onAccount.onblur=function(){
        if(isNaN(Number(oInp.value))){
            alert('不是数字！')
        }
    }
}
