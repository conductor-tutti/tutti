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
    $("#edu_create").click(function(){
        $('.education').append("<div><input type='text' name='education_data'></div>")
        
    });
    $("#edu_delete").click(function(){
        $.ajax({
            url:'/education_delete',
            type: 'POST',
            datatype: "JSON",
            data:{
                data_education_id: $('#edu_delete').attr("data_education_id") 
            },
            success: function(data){
                if (data.success){
                    $("#edu_"+data.edu_id+"").remove()
                    console.log('send msg success!');
                }
                else{
                    console.log('send msg fail!');
                }
            },
            error: function(data){
                console.log("Server error!");
            }
        });
    });
    $("#repertoire_create").click(function(){
        $('.repertoire').append("<div><input type='text' name='repertoire_data'></div>")
    });
    $("#repertoire_delete").click(function(){
        $.ajax({
            url:'/repertoire_delete',
            type: 'POST',
            datatype: "JSON",
            data:{
                data_repertoire_id: $('#repertoire_delete').attr("data_repertoire_id") 
            },
            success: function(data){
                if (data.success){
                    $("#repertoire_"+data.repertoire_id+"").remove()
                    console.log('send msg success!');
                }
                else{
                    console.log('send msg fail!');
                }
            },
            error: function(data){
                console.log("Server error!");
            }
        });
    });
    $("#video_create").click(function(){
        $('.video').append("<div><input type='text' name='video_data'></div>")
    });
    $("#video_delete").click(function(){
        $.ajax({
            url:'/video_delete',
            type: 'POST',
            datatype: "JSON",
            data:{
                data_video_id: $('#video_delete').attr("data_video_id") 
            },
            success: function(data){
                if (data.success){
                    $("#video_"+data.video_id+"").remove()
                    console.log('send msg success!');
                }
                else{
                    console.log('send msg fail!');
                }
            },
            error: function(data){
                console.log("Server error!");
            }
        });
    });
});