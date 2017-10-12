$(function () {
    $("#sign_in").click(function () {
        var username = $("#inputUsername").val()
        var password = $("#inputPassword").val()
        $.ajax({
            type:'POST',
            async:true,
            url:'/login/',
            data:{"user_name":username,"password":password},
            dataType:'json',
            success:function (data) {
                console.log(data)
                if(data.SUCCESS == 'success'){
                    console.log("success")
                    location.href = '/success_login/'
                }

            }
        })

    })

})