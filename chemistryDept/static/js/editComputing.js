$(window).on("load",function(){

   $(".edit-btn").on("click",function(){
     var computing_id = $(this).attr('data-id');
     $("#edit_form").attr("action",`./edit/`+computing_id)
     $.ajax({
         url: `/super-admin/resource/all-computing/get/`+computing_id,
         type: "GET",
         success: (data) => {
           computing_data = JSON.parse(data.data);
           console.log(computing_data);
           $('input[name="computing_heading"]').attr("value",computing_data[0])
           $(`#computing_type_edit option[value=`+computing_data[2]+`]`).attr('selected','selected');
           if(computing_data[2] == "Video"){
              $('input[name="computing_url"]').attr("value",computing_data[1])
           }else{
             $("#computing_image_edit_src").attr("src",`/media/`+computing_data[3])
           }

           if(computing_data[2] == "Video"){
             $("#computing_image_edit").hide();
             $("#computing_video_edit").show();
           }else{
             $("#computing_image_edit").show();
             $("#computing_video_edit").hide();
           }

           $("#computing_type_edit").on("change",function(){
             if(this.value == "Video"){
               $("#computing_image_edit").hide();
               $("#computing_video_edit").show();

             }else if(this.value == "Image"){
               $("#computing_image_edit").show();
               $("#computing_video_edit").hide();
             }
           })
         },
         error: (error) => {
           console.log(error);
         }
        });
   })
})
