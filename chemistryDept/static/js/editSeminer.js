$(window).on('load',()=>{
  // alert("Checking file link");
  //Getting clicked seminer data
  $(".edit-btn").on("click",function(){
    var seminer_id = $(this).attr('data-id');
    //Checking clicked seminer id
    // console.log(seminer_id);
    //Adding the submit form post URL
    $("#edit_form").attr("action",`../edit-seminer/`+seminer_id)
    $.ajax({
        url: `/super-admin/events/seminer/getData/`+seminer_id,
        type: "GET",
        success: (data) => {

          seminer_data = JSON.parse(data.data);
         //Checing the response data
         //console.log(seminer_data);
         //Setting the existing data into form
         $('input[name="seminer_title_edit"]').attr("value",seminer_data[0])
         $('textarea[name="seminer_description_edit"]').val(seminer_data[1])
         tinymce.get('edit_seminer_details').setContent(seminer_data[2]);
         $('input[name="seminer_speakers_edit"]').attr("value",seminer_data[3])
         $('input[name="seminer_location_edit"]').attr("value",seminer_data[5])
          $('textarea[name="seminer_notes_edit"]').val(seminer_data[8])
         $('#datetimepicker2').data("DateTimePicker").date(seminer_data[4]);
         $("#seminer_cover").attr("src",`/media/`+seminer_data[6])
         $('input[name="featured_edit"]').attr("checked",seminer_data[7])
        },
        error: (error) => {
          console.log(error);
        }
       });
  })
})
