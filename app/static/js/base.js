$(document).ready(function(){
    var article_num = 0;

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

    $.ajax({
        url: "/total_article_num",
        dataType: "JSON",
        success: function(data) {
            if(data.article_num){
                article_num = data.article_num;
                $("#total_article_num").append(count);
            }
            else{
                console.log("invalid data")
            }
        },
        error: function(data) {
            console.log("No data at all");
        }
    });
});