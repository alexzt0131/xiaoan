//加载news页面的方法 #

$(function () {
    var mainSection = $("#main");

    $("#admins-news").click(
        function () {
            // alert("click");
            // mainSection.load('news/');
            mainSection.load('news.html');
        }
    );

    $("#addNews").click(
        function () {
            window.location.href='/admins/news/addUI';
        }
    );
});
// function newsUI () {
//     var mainSection = $("#main");
//
//     $("#admins-news").click(
//         function () {
//             alert("click");
//             // mainSection.load('news/');
//         }
//     );
// }
//
