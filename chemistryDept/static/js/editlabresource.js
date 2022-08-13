$(window).on("load",function(){
   $(".edit-btn").on("click",function(){
     var lab_id = $(this).attr('data-id');
     $("#edit_form").attr("action",`./edit/`+lab_id)
     $.ajax({
         url: `/super-admin/resource/all-lab-facility/get/`+lab_id,
         type: "GET",
         success: (data) => {
           get_data = JSON.parse(data.data);
           console.log(get_data);
           $('input[name="image_heading_edit"]').attr("value",get_data[0])
           $('textarea[name="image_caption_edit"]').val(get_data[1])
           $('input[name="lab_image_edit"]').attr("src",get_data[2])
           $("#image_edit").attr("src",`/media/`+get_data[2])
           $(`#lab_sections_edit option[value="`+get_data[3]+`"]`).attr('selected','selected');

          //  faculty_data = JSON.parse(data.data);
          // // console.log(faculty_data);
          //
          //  $('input[name="faculty_name"]').attr("value",faculty_data[0])
          //  $('input[name="faculty_email"]').attr("value",faculty_data[2])
          //  $('input[name="faculty_designation"]').attr("value",faculty_data[3])
          //  $('input[name="faculty_url"]').attr("value",faculty_data[6])
          //  $('textarea[name="faculty_about"]').val(faculty_data[5])
          //  tinymce.get('faculty_experienceedit').setContent(faculty_data[4]);
          //  $('input[name="faculty_image"]').attr("src",faculty_data[1])
          //  $("#faculty_image").attr("src",`/media/`+faculty_data[1])


         },
         error: (error) => {
           console.log(error);
         }
        });
   })
})
