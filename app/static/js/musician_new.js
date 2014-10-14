$(document).ready(function(){
    console.log("Hi! I'm musician_new.js");

    $('#upperCategory').change(function() {
        console.log("You gave me upperCategory data.");

        $.ajax({
            url:'/musician/musician_category/',
            type: 'POST',
            dataType: 'JSON',
            data:{
                uppercategory_data: $('#upperCategory').val()
            },
            success: function(data) {

                subcategory_option = "<option value='none'>선택하세요</option>";

                console.log("success!");
                for (var i = 0; i < data.subcategories.length; i++) {
                    subcategory_option += '<option class="subcategory" value=' + data.subcategories[i][0] + '>' + data.subcategories[i][1] + '</option>';
                }
                console.log($('.subcategory'))
                
                $("#subCategory").html(subcategory_option);
                
            },
            error: function(e) {
                console.log('Something is wrong :(');
            }
        });
    });
    
    $('#upperLocation').change(function() {
        console.log("You gave me upperLocation data.");

        $.ajax({
            url:'/musician/musician_location/',
            type: 'POST',
            dataType: 'JSON',
            data:{
                upperlocation_data :$('#upperLocation').val()
            },
            success: function(data) {

                sublocation_option = "<option value='none'>선택하세요</option>";

                console.log("success!");
                for (var i = 0; i < data.sublocations.length; i++) {
                    sublocation_option += '<option class="sublocation" value=' + data.sublocations[i][0] + '>' + data.sublocations[i][1] + '</option>';
                }
                console.log($('.sublocation'))                
                $("#subLocation").html(sublocation_option);
            },
            error: function(e) {
                console.log('Something is wrong :(');
            }
        });
    });

    var max_fields = 50;
    var wrapper = $(".educationGroup");
    var add_button = $("#addEducationInput");
    var x = 1;
    $(add_button).click(function(e){
        e.preventDefault();
        if(x < max_fields){
            x++;
            console.log(x)
            $(wrapper).append("\
            <div class='row newEducationRow'>\
                <div class='form-group col-md-6 col-md-offset-3'>\
                    <div class='input-group'>\
                        <input class='form-control' placeholder='추가 학력사항'>\
                        <span class='input-group-btn'>\
                            <button id='delEducationInput' type='button' class='btn btn-default'><i class='fa fa-minus'></i></button>\
                        </span>\
                    </div>\
                </div>\
            </div>");
        }
    });

    $(wrapper).on("click", "#delEducationInput", function(e){
        e.preventDefault(); $(this).parent("div").remove(); x--;
    });

    // $("#addEducationInput").click(function(){
    //     // adding input fields dynamically
    //     $('.educationGroup').append("\
    //         <div class='row newEducationRow'>\
    //             <div class='form-group col-md-6 col-md-offset-3'>\
    //                 <div class='input-group'>\
    //                     <input class='form-control' placeholder='추가 학력사항'>\
    //                     <span class='input-group-btn'>\
    //                         <button id='delEducationInput' type='button' class='btn btn-default'><i class='fa fa-minus'></i></button>\
    //                     </span>\
    //                 </div>\
    //             </div>\
    //         </div>");
    // });

    // $("#newEducationRow").click(function(){
    //     $(".newEducationRow").remove();
    // });

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


