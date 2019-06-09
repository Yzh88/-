$(function () {
    $(".sign_in").click(function () {
        alert("签到成功");
        location.href = "/staff_view?in=1"
    })
});
$(function () {
    $(".sign_out").click(function () {
        alert("签退成功");
        location.href = "/staff_view?out=1"
    })
});