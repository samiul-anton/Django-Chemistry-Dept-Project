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
         console.log(seminer_data);
         //Setting the existing data into form
         $('input[name="seminer_title_edit"]').attr("value",seminer_data[0])
         $('textarea[name="seminer_description_edit"]').val(seminer_data[1])
         tinymce.get('edit_seminer_details').setContent(seminer_data[2]);
         $('input[name="seminer_speakers_edit"]').attr("value",seminer_data[3])
         $('input[name="seminer_location_edit"]').attr("value",seminer_data[5])
         //$("#datetimepicker2").data('DateTimePicker').setLocalDate(new Date(seminer_data[4]));

          // $('input[name="faculty_name"]').attr("value",faculty_data[0])
          // $('input[name="faculty_email"]').attr("value",faculty_data[2])
          // $('input[name="faculty_designation"]').attr("value",faculty_data[3])
          // $('input[name="faculty_url"]').attr("value",faculty_data[6])
          // $('textarea[name="faculty_about"]').val(faculty_data[5])
          // tinymce.get('faculty_experienceedit').setContent(faculty_data[4]);
          // $('input[name="faculty_image"]').attr("src",faculty_data[1])
          // $("#faculty_image").attr("src",`/media/`+faculty_data[1])

        },
        error: (error) => {
          console.log(error);
        }
       });
  })
})
