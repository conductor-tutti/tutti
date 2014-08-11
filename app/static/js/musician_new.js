$(document).ready(function(){
    $("#major").hide();
    $("#detailed_profile").hide();
    $("select#select_category").change(function(){
        var selected_category = $("select#select_category > option:selected").val();
        console.log(selected_category)
        if(selected_category == "none")
        {
            // $("#form_submit").empty();
            $("#major").css({"display": "none"});
            $("#detailed_profile").css({"display": "none"});
        }

        else if(selected_category == "Classic")
        {
            $("#major").fadeIn("fast");
            $("select#select_major").change(function(){
                var selected_major = $("select#select_major > option:selected").val();
                console.log(selected_major)
                if(selected_major != "none"){
                    $("#detailed_profile").fadeIn("fast");
                }
                else{
                    $("#detailed_profile").css({"display":"none"});
                }
            });
        }

    function create(selected_major) {
        $("#detailed_profile").fadeIn('fast');
        $("div#registration").append(
            $("#form_submit").append(
                $("<div/>", {id: 'head'}).append(
                    $("<h3/>").text("프로필을 입력하세요")),
                $("<input/>", {
                    type: 'text',
                    placeholder: 'Name',
                    name: 'name_'
                }), $("<br/>"), $("<input/>", {
                    type: 'text',
                    placeholder: 'Email',
                    name: 'email_'
                }), $("<br/>"), $("<textarea/>", {
                    placeholder: 'Message',
                    type: 'text',
                    name: 'msg_'
                }), $("<br/>"), $("<hr/>"), $("<br/>")))
    }

})
});
