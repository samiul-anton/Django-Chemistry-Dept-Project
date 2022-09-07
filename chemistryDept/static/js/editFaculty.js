$(window).on("load",function(){
   $(".edit-btn").on("click",function(){
     var employee_id = $(this).attr('data-id');
     console.log(employee_id);
     $("#edit_form").attr("action",`../edit-faculty/`+employee_id)
     $.ajax({
         url: `/super-admin/people/faculty/getData/`+employee_id,
         type: "GET",
         success: (data) => {

           faculty_data = JSON.parse(data.data);
          // console.log(faculty_data);

           $('input[name="faculty_name"]').attr("value",faculty_data[0])
           $('input[name="faculty_email"]').attr("value",faculty_data[2])
           $('input[name="faculty_designation"]').attr("value",faculty_data[3])
           $('input[name="faculty_url"]').attr("value",faculty_data[6])
           $('textarea[name="faculty_about"]').val(faculty_data[5])
           tinymce.get('faculty_experienceedit').setContent(faculty_data[4]);
           $('input[name="faculty_image"]').attr("src",faculty_data[1])
           $("#faculty_image").attr("src",`/media/`+faculty_data[1])
         },
         error: (error) => {
           console.log(error);
         }
        });
   })
})
