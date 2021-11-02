var myDate = setInterval(myTimer, 1000);

function myTimer() {
  var d = new Date();
  var day=d.getDay();
  var dayOfWeek;
  if(day==0){
      dayOfWeek="Sunday"
  }
  else if(day==1){
      dayOfWeek="Monday"
  }
  else if(day==2){
      dayOfWeek="Tuesday"
  }
  else if(day==3){
      dayOfWeek="Wednesday"
  }
  else if(day==4){
      dayOfWeek="Thursday"
  }
  else if(day==5){
      dayOfWeek="Friday"
  }
  else if(day==6){
      dayOfWeek="Saturday"
  }
  
  document.getElementById("date").innerHTML = dayOfWeek + ", "+ d.toLocaleDateString();
  document.getElementById("time").innerHTML = d.toLocaleTimeString();
}

function imgError(image) {
    image.onerror = "";
    image.src = "https://cdn.wallpapersafari.com/76/96/IRhkld.jpg";
    return true;
}

var isTopics=false;
var isSources=true;
var isCountries=true;

$(document).ready(function(){
    $(".open-topics").click(function(){
        $(".topics").toggle();
        if (isTopics){
            isTopics=!isTopics
            $("#topics").removeClass();
            $("#topics").addClass("glyphicon glyphicon-menu-up");
        }
        else{
            isTopics=!isTopics
            $("#topics").removeClass();
            $("#topics").addClass("glyphicon glyphicon-menu-down");
        }
    })
    $(".open-sources").click(function(){
        $(".sources").toggle();
        if (isSources){
            isSources=!isSources
            $("#sources").removeClass();
            $("#sources").addClass("glyphicon glyphicon-menu-up");
        }
        else{
            isSources=!isSources
            $("#sources").removeClass();
            $("#sources").addClass("glyphicon glyphicon-menu-down");
        }
    })
    $(".open-countries").click(function(){
        $(".countries").toggle();
        if (isCountries){
            isCountries=!isCountries
            $("#countries").removeClass();
            $("#countries").addClass("glyphicon glyphicon-menu-up");
        }
        else{
            isCountries=!isCountries
            $("#countries").removeClass();
            $("#countries").addClass("glyphicon glyphicon-menu-down");
        }
    })
});

