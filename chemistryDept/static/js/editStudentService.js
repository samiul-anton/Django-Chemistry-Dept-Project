$(window).on("load",function(){
   $(".edit-btn").on("click",function(){
     var student_service_id = $(this).attr('data-id');
     console.log(student_service_id);
     $("#edit_form").attr("action",`../all-student-service/edit/`+student_service_id)
     $.ajax({
         url: `/super-admin/resource/all-student-service/get/`+student_service_id,
         type: "GET",
         success: (data) => {
           data = JSON.parse(data.data);
           $('input[name="service_name_edit"]').attr("value",data[0])
           $('input[name="service_link_edit"]').attr("value",data[2])
           $('textarea[name="service_description_edit"]').val(data[1])
           $('input[name="service_cover_edit"]').attr("src",data[3])
           $("#service_cover_edit").attr("src",`/media/`+data[3])
         },
         error: (error) => {
           console.log(error);
         }
        });
   })
})
