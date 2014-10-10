
$(document).ready(function(){
    console.log("Hi!");

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

    $('#upperLocation').change(function() {
        console.log("I'm changed!");

        $.ajax({
            url:'/musician/musician_location/',
            type: 'POST',
            dataType: 'JSON',
            data:{
                location_upper_id :$('#upperLocation').val()
            },
            success: function(data) {
                console.log("succeeded!")

                sublocation_option = "<option value='none'>선택하세요</option>";
                for (var i = 0; i < data.sublocations.length; i++) {
                    sublocation_option += '<option class="sublocation" value=' + data.sublocations[i][0] + '>' + data.sublocations[i][1] + '</option>';
                }
                console.log($('.sublocation'))                
                $("#subLocation").html(sublocation_option);
            },
            error: function(e) {
                console.log('something was wrong :(');
            }
        });
    });
});


