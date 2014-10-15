function addInputField(event) {
    var wrapperClass = $(this).attr("data-target"); // wrapper
    var inputName = $(this).attr("data-name");
    var templateRow = $("#dynamicInputRow").html();
    $(wrapperClass).append(templateRow.replace("^*^inputName^*^", inputName));
    $(".delInput").click(delInputField);
}

function delInputField(event){
    alert("clicked!")
    $(this).parents(".row").remove();
    console.log(this);
}

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

$("#addEducationInput, #addRepertoireInput, #addVideoInput").click(addInputField);

});

