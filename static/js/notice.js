var arr = ["left","top","right","bottom"]
var arr1 = ["left","bottom","right","top"]
var index = 0;
function autorun(){
    var utive1 = "border-"+arr1[index];
    var utive = "border-"+arr[index];

    $("#inner1").css("border","5px solid blue");
    $("#inner2").css("border","5px solid blue");
    $("#inner3").css("border","5px solid blue");
    $(".top1").css("border","1px solid blue");
    index++;
    if(index==arr.length){
        index=0;
    }
    $("#inner1").css(utive,"5px solid red");
    $("#inner2").css(utive1,"5px solid red");
    $("#inner3").css(utive1,"5px solid red");
    $(".top1").css(utive1,"5px solid red");
}

$(function (){
   timer = setInterval(autorun,500);
    $("#show_notice").click(function (){
        $("#inner1").css("display","block");
        $("#inner2").css("display","none");
    })

     $("#find_notice").click(function (){

        $("#inner1").css("display","none");
        $("#inner2").css("display","block");
        })

     $("#inner1").mouseover(function (){
            clearInterval(timer);
         });
     $("#inner2").mouseover(function (){
             clearInterval(timer);
          });
     $("#inner1").mouseout(function (){
             timer = setInterval(autorun,500);
          });
     $("#inner2").mouseout(function (){
             timer = setInterval(autorun,500);
           })

})