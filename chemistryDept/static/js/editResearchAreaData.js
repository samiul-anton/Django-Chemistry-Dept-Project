$(window).on("load",function(){
   $(".edit-btn").on("click",function(){
     var data_id = $(this).attr('data-id');
     $("#edit_form").attr("action",`../by-area/edit-research-area/`+data_id)
     $.ajax({
         url: `/super-admin/research/by-area/getData/`+data_id,
         type: "GET",
         success: (data) => {

           research_data = JSON.parse(data.data);
           $('input[name="research_title"]').attr("value",research_data[2])
           $('textarea[name="research_description"]').val(research_data[3])
           $(`#selectResearchFields option[value=`+research_data[0]+`]`).attr('selected','selected');
           $('input[name="publication_video"]').attr("value",research_data[5]);
           tinymce.get('research_includee').setContent(research_data[4]);
           tinymce.get('publication_detailss').setContent(research_data[6]);
           $("#research_cover").attr("src",`/media/`+research_data[1])
         },
         error: (error) => {
           console.log(error);
         }
        });
   })
})
