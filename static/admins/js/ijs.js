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
//news页面确认删除跳转的方法
function checkDel(uuid){
    if(confirm('确认要删除吗?')){
        window.location.href="/admins/newsMethods?m=del&id="+uuid;
    }else{
        return
    }
}


