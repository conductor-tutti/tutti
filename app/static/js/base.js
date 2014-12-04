$(document).ready(function(){
    $("#comment_create").click(function(){
        $.ajax({
            url:'/comment_create',
            type: 'POST',
            datatype: "JSON",
            data:{
                comment_data: $('#comment').val(),
                musician_id_data: $('#comment').attr("data-musician-id")
            },
            success: function(data){
                if (data.success){
                    $('#comment_row').append(
                        "<div class='comment'>" + "<strong>" +
                        "<i class='author_name'>" + data.author_name + "</i>"
                        + "</strong>" + "<br>" + data.comment_data + "</div>")
                    $('#comment').val("");
                    console.log('send msg success!');
                }
            }
        }); 
    });
});