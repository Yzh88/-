//点击显示数据
function show_recruit1(){
    $("#table2").css("display","none");
    $("#table3").css("display","none");
    $("#content").css("display","none");
    $("#table1").css("display","");
}
function show_recruit2(){
    $("#table1").css("display","none");
    $("#table3").css("display","none");
    $("#content").css("display","none");
    $("#table2").css("display","");
}
function show_recruit3(){
    $("#table1").css("display","none");
    $("#table2").css("display","none");
    $("#content").css("display","none");
    $("#table3").css("display","");
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
