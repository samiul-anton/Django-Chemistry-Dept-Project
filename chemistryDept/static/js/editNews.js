$(window).on("load",function(){
   $(".edit-btn").on("click",function(){
     var news_id = $(this).attr('data-id');
     console.log(news_id);
     $("#edit_form").attr("action",`../news/edit-news/`+news_id)
     $.ajax({
         url: `/super-admin/news/getData/`+news_id,
         type: "GET",
         success: (data) => {

           news_data = JSON.parse(data.data);
           console.log(news_data);

           $('input[name="news_title_edit"]').attr("value",news_data[0])
           $('textarea[name="news_description_edit"]').val(news_data[2])
           $('input[name="news_category_edit"]').attr("value",news_data[3])
           $('input[name="news_url_edit"]').attr("value",news_data[4])

           $('input[name="news_cover_edit"]').attr("src",news_data[1])
           $("#newsCover").attr("src",`/media/`+news_data[1])
         },
         error: (error) => {
           console.log(error);
         }
        });
   })
})
