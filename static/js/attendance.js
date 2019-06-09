//点击显示数据
function show_inner1(){
    $("#table2").css("display","none");
    $("#table3").css("display","none");
    $("#table4").css("display","none");
    $("#content").css("display","none");
    $("#table1").css("display","");
}
function show_inner2(){
    $("#table1").css("display","none");
    $("#table3").css("display","none");
    $("#table4").css("display","none");
    $("#content").css("display","none");
    $("#table2").css("display","");
}
function show_inner3(){
    $("#table1").css("display","none");
    $("#table2").css("display","none");
    $("#table4").css("display","none");
    $("#content").css("display","none");
    $("#table3").css("display","");
}
function show_inner4(){
    $("#table1").css("display","none");
    $("#table2").css("display","none");
    $("#table3").css("display","none");
    $("#content").css("display","none");
    $("#table4").css("display","");
}



//隐藏数据
function dele1() {
    $("#table1").css("display","none");
    $("#content").css("display","");
}
function dele2() {
    $("#table2").css("display","none");
    $("#content").css("display","");
}
function dele3() {
    $("#table3").css("display","none");
    $("#content").css("display","");
}
function dele4() {
    $("#table4").css("display","none");
    $("#content").css("display","");
}


//
var arr = ["left","top","right","bottom"]
var arr1 = ["left","bottom","right","top"]
var index = 0;
function autorun(){
    var utive1 = "border-"+arr1[index];
    var utive = "border-"+arr[index];

    $("#inner1").css("border","5px solid blue");
    $("#inner2").css("border","5px solid blue");
    $("#inner3").css("border","5px solid blue");
    $(".top1").css("border","5px solid blue");


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
    var isactive = false;
    $("#left_notice").click(function (){
        isactive = !isactive;
        if(isactive){
            $("#inner1").css("display","none");
            $("#inner2").css("display","block");
        }else{
            $("#inner1").css("display","block");
            $("#inner2").css("display","none");
        }
    })
})