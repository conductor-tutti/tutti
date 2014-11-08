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
        $.ajax({
            url:'/education_create',
            type: 'POST',
            datatype: "JSON",
            data:{
                edu_data: $('#edu_data').val(),
                data_musician_id: $('#edu_data').attr("data_musician_id") 
            },
            success: function(data){
                if (data.success){
                    $('.education').append("<div id='edu_"+
                        data.edu_id+"'>"+data.edu_data+
                        "<button id='edu_delete' type='button' data_education_id='"
                        +data.edu_id+"'>삭제</button><button id='edu_update' type='button' data_education_id='"
                        +data.edu_id+"'>수정</button>")
                    $('#edu_data').val("");
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
        $.ajax({
            url:'/repertoire_create',
            type: 'POST',
            datatype: "JSON",
            data:{
                repertoire_data: $('#repertoire_data').val(),
                data_musician_id: $('#repertoire_data').attr("data_musician_id") 
            },
            success: function(data){
                if (data.success){
                    $('.repertoire').append("<div id='repertoire_"+
                        data.repertoire_id+"'>"+data.repertoire_data+
                        "<button id='repertoire_delete' type='button' data_repertoire_id='"
                        +data.repertoire_id+"'>삭제</button><button id='repertoire_update' type='button' data_repertoire_id='"
                        +data.repertoire_id+"'>수정</button>")
                    $('#repertoire_data').val("");
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
        $.ajax({
            url:'/video_create',
            type: 'POST',
            datatype: "JSON",
            data:{
                video_data: $('#video_data').val(),
                data_musician_id: $('#video_data').attr("data_musician_id") 
            },
            success: function(data){
                if (data.success){
                    $('.video').append("<div id='video_"+
                        data.video_id+"'>"+data.video_data+
                        "<button id='video_delete' type='button' data_video_id='"
                        +data.video_id+"'>삭제</button><button id='video_update' type='button' data_video_id='"
                        +data.video_id+"'>수정</button>")
                    $('#video_data').val("");
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