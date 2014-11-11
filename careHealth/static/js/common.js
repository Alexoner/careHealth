function loginModal(){
    $("#login_btn").click(function(){
        var user = $("#login_user").val();
        var pass = $("#login_pass").val();
        var login_callback  = function(){
            alert("这是模拟登陆，没有发出ajax请求");
            $(".after_login").css('display','block');
            $(".before_login").css('display','none');
            $("#loginModal").modal('hide');
        };
        if(user.trim().length <= 0){
            alert("please input the right user name");
            return;
        }
        if(pass.trim().length <= 0){
            alert("please input the password");
            return;
        }
        //$.post();
        login_callback();
    });
}
