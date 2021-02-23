// получаем все элементы
var videoEl = document.getElementsByTagName('video')[0],
    timePicker = document.getElementById('timer'),
    subs = document.getElementById('subtitles'),
    sub = document.getElementById('sub_text'),
    translate = document.getElementById('sub_translate'),
    curId = 0;


var flag = null;

$.getJSON('static/data.json', function(data) {
    videoEl.addEventListener('timeupdate', function () {
            for (var i = 0; i < data.length; i++) {
                if (data[i].time_start < videoEl.currentTime && data[i].time_end > videoEl.currentTime) {
                    if (flag != i) {
                        sub.innerHTML = '';
                        text = []
                        text_ru = []
                        for (var j = 0; j < data[i].text.length; j++) {
                            sub.innerHTML += "<span class=\"sub_word\" id=\"sub_" + j + "\">" + data[i].text[j] + "</span>";
                            text.push(data[i].text[j]);
                            text_ru.push(data[i].text_ru[j]);
                        }
                        sub.onmouseover = function(event){
                            translate.innerHTML = text_ru[parseInt(event.target.id.slice(4), 10)];
                        };
                        sub.onmouseout = function(event){
                            translate.innerHTML = "";
                        };
                        subs.onmousedown = function(event){
                            sub.innerHTML = "asssssssssssssssssssssssssssssssssssssssssssssssssssssss";
                        };
                        subs.onmouseup = function(event){
                            sub.innerHTML = '';
                            for (var j = 0; j < data[i].text.length; j++) {
                                sub.innerHTML += "<span class=\"sub_word\" id=\"sub_" + j + "\">" + data[i].text[j] + "</span>";
                            }
                        };
                        flag = i;
                    }
                }
            }
    }, false);
});
/*
document.getElementById(sub_ru_id).onmouseover = function() {
    .classList.remove('hidden');
}
raz1.onmouseout = function(e) {
    .classList.add('hidden');
}
*/

