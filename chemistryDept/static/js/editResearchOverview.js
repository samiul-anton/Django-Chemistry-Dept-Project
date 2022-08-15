$(window).on("load",function(){
   $(".edit-btn").on("click",function(){
     var data_id = $(this).attr('data-id');
     $("#edit_form").attr("action",`../overview/edit/`+data_id)
     $.ajax({
         url: `/super-admin/research/overview/getData/`+data_id,
         type: "GET",
         success: (data) => {
           project_data = JSON.parse(data.data);
           $(`#overview_facutly option[value=`+project_data[0]+`]`).attr('selected','selected');
           $('input[name="sustainability"]').attr("value",project_data[1]);
           $('input[name="energy"]').attr("value",project_data[2]);
           $('input[name="artificial_itelligence"]').attr("value",project_data[3]);
           $('input[name="education"]').attr("value",project_data[4]);
           $('input[name="biomedical"]').attr("value",project_data[5]);
         },
         error: (error) => {
           console.log(error);
         }
        });
   })
})
