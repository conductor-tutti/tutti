$(document).ready(function(){

    $('#sido').change(function() {
        $.ajax({
            url:'/musician/musician_new/',
            type: 'POST',
            dataType: 'JSON',
            data:{
                location:$('#sido').val()

            },
            success: function(data) {
                console.log gotj
                sigungu += '<option>' + sigungu + '</option>';
                $("#sigungu").append(sigungu);
            }

            error : function(data) {
                    console.log('Server error!!')
                }
            })
    })
})









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
