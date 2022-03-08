function initRate(){



}
function selectYouxi(obj){
    if (obj)
    window.location.href="../view/?id="+$(obj).val()
}
function toByBotton(){
    window.location.href="https://www.baidu.com"
}
function initYouxi(){
        $.ajax({
            //请求方式
            type : "GET",
            //请求的媒体类型
            //请求地址
            url : "../queryByGameName/",
            //数据，json字符串
            dataType : "JSON",
            //请求成功
            success : function(result) {
                console.log(result)
            var html ="";
                html+="<option value=''>Select Game</option>"
            for (var i = 0; i<result.length;i++){
                html+="<option value='"+result[i].pk+"'>"+result[i].fields.name+"</option>"
            }
            $("#myselect").html(html)

            },
            //请求失败，包含具体的错误信息
            error : function(e){
                console.log(e.status);
                console.log(e.responseText);
            }
        });
}
$(function(){
			initRate()
        initYouxi()
});

