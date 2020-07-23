
function js_method(word) {
    var txt2 = $("<audio></audio>").attr({ "src": "http://dict.youdao.com/dictvoice?audio=" + word + "&type=1", "autoplay": "autoplay" });
    $(".words").append(txt2);
    var len = $(".words").children().length;
    // console.log(len);
    if (len >= 3) {
        $("audio").eq(0).remove()
    }


}

