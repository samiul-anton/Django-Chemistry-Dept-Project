$(window).on("load",function(){
   $(".edit-btn").on("click",function(){
     var staff_id = $(this).attr('data-id');
     $("#edit_form").attr("action",`../edit-staff/`+staff_id)
     $.ajax({
         url: `/super-admin/people/staff/getData/`+staff_id,
         type: "GET",
         success: (data) => {

           staff_data = JSON.parse(data.data);
           console.log(staff_data);

           $('input[name="staff_name"]').attr("value",staff_data[0])
           $('input[name="staff_email"]').attr("value",staff_data[2])
           $('input[name="staff_designation"]').attr("value",staff_data[3])
           $('input[name="staff_image"]').attr("src",staff_data[1])
           $("#staff_image").attr("src",`/media/`+staff_data[1])
           $('textarea[name="staff_description"]').val(staff_data[4])
         },
         error: (error) => {
           console.log(error);
         }
        });
   })
})
