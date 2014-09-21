 $(document).ready(function(){
     var article_num = 0;
     var current_row = 2;

     $("#bt_calculate").bind("click", function(){

         $.ajax({
             url: "/test",
             type: "POST",  type: default is "GET"
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
                 $("#total_article_num").append(article_num.toString() + "개의 게시물이 있으심");
             }
             else{
                 console.log("You have no total article number data at all")
             }
         },
         error: function(data) {
             console.log("No data at all!!!!");
         }
     });

     $("#more_btn").click(function(){
         $.ajax({
             url: "/more_article",
             dataType: "JSON",
             data: {
                 current_row: current_row,
                 article_num: article_num
             },
             success: function(data){
                 current_row += 1;
                 called_articles = data.data;
                 for(var i in called_articles){
                     article = called_articles[i];
                     string = "<div class='well' id='article_"+article.id+"'>
                     <h1><a href='article/detail/"+article.id"'>"+article.title+"</a></h1><h3>"
                     +article.author+"</h3><h6>"+article.content+"</h6></div>";
                     console.log(string)
                     $("#called_articles_list").append(string);

                     if("#called_articles_list" != 1){
                         $("#more_btn").hide();
                         $("#called_articles_list").append("글 엄씀 이제");
                     }
                 },
                 error: function(data){
                     console.log("invalid data")
                 }
             }
         });
     });
 });