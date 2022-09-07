$(window).on("load",function(){
   $(".edit-btn").on("click",function(){
     var course_id = $(this).attr('data-id');
     $("#edit_form").attr("action",`../edit-course/`+course_id)
     $.ajax({
         url: `/super-admin/events/courses/getData/`+course_id,
         type: "GET",
         success: (data) => {
           data = JSON.parse(data.data);
           $('input[name="course_name_edit"]').attr("value",data[0])
           $('input[name="instructor_name_edit"]').attr("value",data[1])
           $('input[name="number_of_credit_edit"]').attr("value",data[3])
           tinymce.get('course_description_edit').setContent(data[2]);
           tinymce.get('course_content_edit').setContent(data[5]);
           $('input[name="course_cover_edit"]').attr("src",data[4])
           $("#course_cover_preview").attr("src",`/media/`+data[4])

         },
         error: (error) => {
           console.log(error);
         }
        });
   })
})
