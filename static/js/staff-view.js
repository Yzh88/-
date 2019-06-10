$(function () {
    $(".sign_in").click(function () {
        alert("签到成功");
        location.href = "/staff_view?in="+$("#id").val()
    })
});
$(function () {
    $(".sign_out").click(function () {
        alert("签退成功");
        location.href = "/staff_view?out="+$("#id").val()
    })
});