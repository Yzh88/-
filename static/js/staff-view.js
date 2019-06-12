$(function () {
    $('.sign_in').click(function () {
        $.ajax({
            url: "/staff_view",
            type: "post",
            async: true,
            data:{
                sign:$("#id").val(),
                key:'in'
            },
            dataType: "json",
            success: function (data) {
                alert(data);
            }
        });
    });
    $('.sign_out').click(function () {
        $.ajax({
            url: "/staff_view",
            type: "post",
            async: true,
            data:{
                sign:$("#id").val(),
                key:'out'
            },
            dataType: "json",
            success: function (data) {
                alert(data);
            }
        })
    })
});
