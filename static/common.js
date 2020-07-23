
function js_method(word) {
    var txt2 = $("<audio></audio>").attr({ "src": "http://dict.youdao.com/dictvoice?audio=" + word + "&type=1", "autoplay": "autoplay" });
    $(".words").append(txt2);
    // setTimeout(function(){
    //     $("audio").remove();
    //     },3000);
    if ($("audio").lenght>3) {
        $("audio").eq(0).remove();
    }
}

