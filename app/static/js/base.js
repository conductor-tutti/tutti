$(document).ready(function(){
    $("#bt_calculate").bind("click", function(){

        $.ajax({
            url: "/test",
            type: "POST", // type: default is "GET"
            data: { input_first: $('input[name="input_first"]').val(),
                    input_second: $('input[name="input_second"]').val() },
            dataType: "JSON",
            success: function(data) {
                $("#result").text(data.result);
                console.log("#result")
            }
        });
        return false;
    });

});