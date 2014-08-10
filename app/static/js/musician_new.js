$(document).ready(function(){
 
 $('select#select_btn').change(function(){
 
 var sel_value = $('option:selected').val();
 if(sel_value==0)
 {
 //Resetting Form
 $("#form_submit").empty();
 $("#form1").css({'display':'none'});
 }
 else{
 //Resetting Form
 $("#form_submit").empty();
 
 //Below Function Creates Input Fields Dynamically
 create(sel_value);
 
 //appending submit button to form
 $("#form_submit").append(
 $("<input/>",{type:'submit', value:'Register'})
 )
 }
 }); 
 
function create(sel_value){
 for(var i=1;i<=sel_value;i++)
 {
 $("div#form1").slideDown('slow');
 
 $("div#form1").append(
 $("#form_submit").append(
 $("<div/>",{id:'head'}).append(
 $("<h3/>").text("Registration Form"+i)),
 $("<input/>", {type:'text', placeholder:'Name'+i, name:'name_'+i}),
 $("<br/>"),
 $("<input/>", {type:'text', placeholder:'Email'+i, name:'email_'+i}),
 $("<br/>"),
 $("<textarea/>", {placeholder:'Message'+i, type:'text', name:'msg_'+i}),
 $("<br/>"),
 $("<hr/>"),
 $("<br/>")
 ))
 }
 
 }
 
});