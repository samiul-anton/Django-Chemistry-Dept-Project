$(window).on("load",function(){
   $(".edit-btn").on("click",function(){
     var data_id = $(this).attr('data-id');
     console.log(data_id);
     //$("#edit_form").attr("action",`../by-area/edit-research-area/`+data_id)
     $.ajax({
         url: `/super-admin/research/by-direction/getData/`+data_id,
         type: "GET",
         success: (data) => {
           project_data = data.data;
           $('input[name="project_name"]').attr("value",project_data[4]);
           $(`#research_direction_fields option[value=`+project_data[0]+`]`).attr('selected','selected');
           // $('textarea[name="research_description"]').val(project_data[3])

           // $('input[name="publication_video"]').attr("value",project_data[5]);
           // tinymce.get('research_includee').setContent(project_data[4]);
           // tinymce.get('publication_detailss').setContent(project_data[6]);
           // $("#research_cover").attr("src",`/media/`+project_data[1])
         },
         error: (error) => {
           console.log(error);
         }
        });
   })
})
