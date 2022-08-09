$(window).on("load",function(){
   $(".edit-btn").on("click",function(){
     var computing_id = $(this).attr('data-id');
     $("#edit_form").attr("action",`../edit/`+computing_id)
     $.ajax({
         url: `/super-admin/resource/all-computing/get/`+computing_id,
         type: "GET",
         success: (data) => {

           computing_data = JSON.parse(data.data);
           console.log(computing_data);

           $('input[name="computing_heading"]').attr("value",computing_data[0])
           $(`#computing_type option[value=`+computing_data[2]+`]`).attr('selected','selected');
           // $('input[name="faculty_email"]').attr("value",computing_data[2])
           // $('input[name="faculty_designation"]').attr("value",computing_data[3])
           // $('input[name="faculty_url"]').attr("value",computing_data[6])
           // $('textarea[name="faculty_about"]').val(computing_data[5])
           // tinymce.get('faculty_experienceedit').setContent(computing_data[4]);
           // $('input[name="faculty_image"]').attr("src",computing_data[1])
           // $("#faculty_image").attr("src",`/media/`+computing_data[1])
         },
         error: (error) => {
           console.log(error);
         }
        });
   })
})
