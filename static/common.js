

document.ready(function() {
    var voice = document.getElementById('voice'); //获取到audio元素
        document.getElementsByClassName("but").click(function() { //点击文字事件
        
            voice.play(); //音乐播放
            
        });
    });
