function addInputField(event) {
    var wrapperClass = $(this).attr("data-target"); // wrapper
    var inputName = $(this).attr("data-name");
    var templateRow = $("#dynamicInputRow").html();
    $(wrapperClass).append(templateRow.replace("^*^inputName^*^", inputName));
    $(".delInput").click(delInputField);
}

function delInputField(event){
    $(this).parents(".row").remove();
    console.log(this);
}

function formValidate(event){
    if(document.profileForm.uppercategory.value == "none"){
        alert("전공분야를 선택해주세요.");
        document.profileForm.uppercategory.focus();
        return false;
    }
    if(document.profileForm.subcategory.value == "none"){
        alert("세부전공을 선택해주세요.");
        document.profileForm.subcategory.focus();
        return false;
    }
    if(document.profileForm.upperlocation.value == "none"){
        alert("거주지역을 선택해주세요.");
        document.profileForm.upperlocation.focus();
        return false;
    }
    if(document.profileForm.sublocation.value == "none"){
        alert("세부지역을 선택해주세요.");
        document.profileForm.sublocation.focus();
        return false;
    }
    if (document.profileForm.phrase.value == ""){
        alert("50자 메시지는 필수에요!");
        document.profileForm.phrase.focus();
        return false;
    }

    // validating videoInput part is weird!

    for (i = 0; i < document.profileForm.videoInput.length; i++) { 
        if (document.profileForm.videoInput[i].value == ""){
            console.log(document.profileForm.videoInput[i].value)
            alert("비디오 URL을 입력하세요. 혹은 필요없는 입력란을 지워주세요.")
            document.profileForm.videoInput[i].focus();
            return false;
        }
    }
    alert("서밋으로 가버렷!")
    return(true);
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
$(".delInput").click(delInputField);
$("#submit").click(formValidate);
});

