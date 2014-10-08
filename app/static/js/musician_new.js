
$(document).ready(function(){
    console.log("I'm ready!");
    $('#location').change(function() {
        console.log("I'm changed!");

        $.ajax({
            url:'/musician/musician_location/',
            type: 'POST',
            dataType: 'JSON',
            data:{
                location:$('#location').val()
            },
            success: function(data) {
                
                sigungu = "<option value='none'>선택하세요</option>";

                console.log("success!");
                for (var i = 0; i < data.locations.length; i++) {
                    sigungu += '<option class="sublocation" value=' + data.locations[i][0] + '>' + data.locations[i][1] + '</option>';
                }
                console.log($('.sublocation'))                
                $("#location_detail").html(sigungu);
            },
            error: function(e) {
                console.log('Server error!!');
            }
        });
    });

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


