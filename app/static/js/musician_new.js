
$(document).ready(function(){
    console.log("I'm ready!");
    $('#sido').change(function() {
        console.log("I'm changed!");

        $.ajax({
            url:'/musician/musician_location/',
            type: 'POST',
            dataType: 'JSON',
            data:{
                location:$('#sido').val()
            },
            success: function(data) {
                
                sigungu = "<option value='none'>선택하세요</option>";

                console.log("success!");
                for (var i = 0; i < data.locations.length; i++) {
                    sigungu += '<option class="sublocation" value=' + data.locations[i][0] + '>' + data.locations[i][1] + '</option>';
                }
                console.log($('.sublocation'))
                
                $("#sigungu").html(sigungu);
                
            },
            error: function(e) {
                console.log('Server error!!');
            }
        });
    });
});


$(document).ready(function(){
    console.log("I'm ready!");
    $('#category').change(function() {
        console.log("I'm changed!");

        $.ajax({
            url:'/musician/musician_category/',
            type: 'POST',
            dataType: 'JSON',
            data:{
                category:$('#category').val()
            },
            success: function(data) {
                
                major = "<option value='none'>선택하세요</option>";

                console.log("success!");
                for (var i = 0; i < data.categories.length; i++) {
                    major += '<option class="major" value=' + data.categories[i][0] + '>' + data.categories[i][1] + '</option>';
                }
                console.log($('.major'))
                
                $("#major").html(major);
                
            },
            error: function(e) {
                console.log('Server error!!');
            }
        });
    });
});




// $(document).ready(function(){
//     $("#major-group").hide();
//     $("#detail-group").hide();
//     $("select#select_category").change(function(){
//         var selected_category = $("select#select_category > option:selected").val();
//         console.log(selected_category)
//         if(selected_category == "none")
//         {
//             // $("#form_submit").empty();
//             $("#major-group").css({"display": "none"});
//             $("#detail-group").css({"display": "none"});
//         }

//         else if(selected_category == "Classic")
//         {
//             $("#major-group").fadeIn("fast");
//             $("select#select_major").change(function(){
//                 var selected_major = $("select#select_major > option:selected").val();
//                 console.log(selected_major)
//                 if(selected_major != "none"){
//                     $("#detail-group").fadeIn("fast");
//                 }
//                 else{
//                     $("#detail-group").css({"display":"none"});
//                 }
//             });
//         }
//     })

//     function preventEnter(event){
//         var event = (event) ? event : ((event) ? event : null);
//         var node = (event.target) ? event.target : ((event.srcElement) ? event.srcElement : null);
//         if ((event.KeyCode == 13) && (node.type=="text")) {return false;}
//     }

//     function create(selected_major) {
//         $("#detailed_profile").fadeIn('fast');
//         $("div#registration").append(
//             $("#form_submit").append(
//                 $("<div/>", {id: 'head'}).append(
//                     $("<h3/>").text("프로필을 입력하세요")),
//                 $("<input/>", {
//                     type: 'text',
//                     placeholder: 'Name',
//                     name: 'name_'
//                 }), $("<br/>"), $("<input/>", {
//                     type: 'text',
//                     placeholder: 'Email',
//                     name: 'email_'
//                 }), $("<br/>"), $("<textarea/>", {
//                     placeholder: 'Message',
//                     type: 'text',
//                     name: 'msg_'
//                 }), $("<br/>"), $("<hr/>"), $("<br/>")))
//     }

// });
