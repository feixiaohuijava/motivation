var jsonstr = [{"a":"dema","b":"guanghui"},{"c":"timo","d":"xiaopao"}]


$(function a() {
    $.ajax({
        type:"GET",
        async:true,
        url:'/send_data_to_ajax/',
        dataType:'json',
        jsonp:'callback',
        success:function (data) {
            console.log(data);
            a();

        }
    })

})


function getData(idArr, i){

    if (idArr.length) {
        var id = idArr[0];
        var url = getUrl(hqData.api,id);
        console.log(i, 111)
        $.ajax({
            type: "GET",
            url: url,
            dataType: "jsonp",
            jsonp:'cb',
            async: true, //这里异步就好了
            success:function(json){
                if(!!json&& typeof json[0]=='string'){
                    console.log(json,222)
                }
                getData(idArr.shift(), ++i); //回调成功再进入下一次递归
            },
            error: function() {
                getData(idArr.shift(), ++i); //如果ajax请求失败仍需要继续下一步递归
            }
        })
    }

}

getData(hqData.idArr, 0)