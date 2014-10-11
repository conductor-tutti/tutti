
$(document).ready(function(){
    console.log("Hi!");

    $('#upperCategory').change(function() {
        console.log("You gave me upperCategory data.");

        $.ajax({
            url:'/musician/musician_category/',
            type: 'POST',
            dataType: 'JSON',
            data:{
                uppercategory: $('#upperCategory').val()
            },
            success: function(data) {

                subcategory_option = "<option value='none'>선택하세요</option>";

                console.log("success!");
                for (var i = 0; i < data.categories.length; i++) {
                    subcategory_option += '<option class="subcategory" value=' + data.subcategories[i][0] + '>' + data.subcategories[i][1] + '</option>';
                }
                console.log($('.subcategory'))
                
                $("#subCategory").html(major);
                
            },
            error: function(e) {
                console.log('Something is wrong :(');
            }
        });
    });
    
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
});


