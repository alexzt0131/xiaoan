//加载news页面的方法 #

/**
 * onload的方法
 */
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
            window.location.href = '/admins/news/addUI';
        }
    );

    //判断新闻修改页面是否input 是否已经选定上传文件
    // $("#uploadInput").change(function () {
    //     var file = $(this).val();
    //     if (file) {
    //         // alert('已经选定上传文件！');
    //         window.console.log(file);
    //     }
    // });


    $(function () {
        //将fileinput选定的图片直接预览显示在指定的img中
        $("#uploadInput").on("change", function () {
            var $file = $(this);
            var fileObj = $file[0];
            var windowURL = window.URL || window.webkitURL;
            var dataURL;
            // var $img = $("img");
            var img = $("#newsPhoto");
            if (fileObj && fileObj.files && fileObj.files[0]) {
                dataURL = windowURL.createObjectURL(fileObj.files[0]);
                img.attr('src', dataURL);
            } else {
                dataURL = $file.val();
                var imgObj = document.getElementById("preview");
                imgObj.style.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale)";
                imgObj.filters.item("DXImageTransform.Microsoft.AlphaImageLoader").src = dataURL;
            }
            // window.console.log(fileObj.files)

            //将文件ajax发送到服务器
            //文件上传(成功)
            var uploadNewsPic = fileObj;
            // window.console.log(uploadNewsPic);
            $.ajaxFileUpload
            ({
                url: '/upload/?module=news', //用于文件上传的服务器端请求地址
                secureuri: false, //是否需要安全协议，一般设置为false
                fileElementId: 'uploadInput', //文件上传域的ID
                dataType: 'json', //返回值类型 一般设置为json
                data: {uploadNewsPic: uploadNewsPic}, //传递参数到服务器
                success: function (data)  //服务器成功响应处理函数
                {
                    window.console.log('请求数据成功!');
                    window.console.log(data['filename']);
                    $('#hidFilename').val(data['filename'])

                },
                error: function (data, status, e)//服务器响应失败处理函数
                {
                    window.console.log('请求数据失败!');
                    window.console.log(data);
                    window.console.log(status);
                    window.console.log(e);

                }
            });


        });
    });

    $(function () {
        //将fileinput选定的图片直接预览显示在指定的img中
        $("#uploadInput1").on("change", function () {
            var $file = $(this);
            var fileObj = $file[0];
            var windowURL = window.URL || window.webkitURL;
            var dataURL;
            // var $img = $("img");
            var img = $("#newsPhoto");
            if (fileObj && fileObj.files && fileObj.files[0]) {
                dataURL = windowURL.createObjectURL(fileObj.files[0]);
                img.attr('src', dataURL);
            } else {
                dataURL = $file.val();
                var imgObj = document.getElementById("preview");
                imgObj.style.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale)";
                imgObj.filters.item("DXImageTransform.Microsoft.AlphaImageLoader").src = dataURL;
            }
        });
    });
});

// //文件上传(成功)
// function uploadNewsPic() {
//     var uploadNewsPic = fileObj;
//     window.console.log(uploadNewsPic);
//     $.ajaxFileUpload
//     ({
//         url: '/upload/?module=news', //用于文件上传的服务器端请求地址
//         secureuri: false, //是否需要安全协议，一般设置为false
//         fileElementId: 'uploadInput', //文件上传域的ID
//         dataType: 'json', //返回值类型 一般设置为json
//         data: {uploadNewsPic: uploadNewsPic}, //传递参数到服务器
//         success: function (data, status)  //服务器成功响应处理函数
//         {
//             window.console.log('请求数据成功!');
//             window.console.log(status);
//
//         },
//         error: function (data, status, e)//服务器响应失败处理函数
//         {
//             window.console.log('请求数据成功!');
//         }
//     });
// }

//news页面确认删除跳转的方法
function checkDel(uuid) {
    if (confirm('确认要删除吗?')) {
        window.location.href = "/admins/newsMethods?m=del&id=" + uuid;
    } else {
        return
    }
}





