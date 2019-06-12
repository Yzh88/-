$(function () {
    $('.sign_in').click(function () {
        $.ajax({
            url:"/staff_view?in="+$("#num").val(),
            type:"get",
            async:true,
            dataType:"json",
            success:function (data) {
                alert(data)
            }
        })
    })
});
$(function () {
    $('.sign_out').click(function () {
        $.ajax({
            url:"/staff_view?out="+$("#num").val(),
            type:"get",
            async:true,
            dataType:"json",
            success:function (data) {
                alert(data)
            }
        })
    })
});