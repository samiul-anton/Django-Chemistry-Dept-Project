$(window).on("load",function(){
   $(".edit-btn").on("click",function(){
     var student_id = $(this).attr('data-id');
     $("#edit_form").attr("action",`../edit-student/`+student_id)
     $.ajax({
         url: `/super-admin/people/student/getData/`+student_id,
         type: "GET",
         success: (data) => {

           student_data = JSON.parse(data.data);
           $('input[name="student_name"]').attr("value",student_data[0])
           $('input[name="student_email"]').attr("value",student_data[2])
           $('input[name="staff_image"]').attr("src",student_data[1])
           $("#student_image").attr("src",`/media/`+student_data[1])
           $(`#selectDegree option[value=`+student_data[3]+`]`).attr('selected','selected');
         },
         error: (error) => {
           console.log(error);
         }
        });
   })
})
