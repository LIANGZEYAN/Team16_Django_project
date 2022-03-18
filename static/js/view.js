function initRate(){



}
function selectYouxi(obj){
    if (obj)
    window.location.href="../view/?id="+$(obj).val()
}

function initYouxi(){
        $.ajax({

            type : "GET",
            url : "../queryByGameName/",
            dataType : "JSON",
            success : function(result) {
                console.log(result)
            var html ="";
                html+="<option value=''>Select Game</option>"
            for (var i = 0; i<result.length;i++){
                html+="<option value='"+result[i].pk+"'>"+result[i].fields.name+"</option>"
            }
            $("#myselect").html(html)

            },
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

