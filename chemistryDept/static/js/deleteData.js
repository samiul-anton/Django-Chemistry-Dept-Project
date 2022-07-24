$(window).on('load', function() {

    $('.del-btn').on("click",function(){
        $("#delete-form").attr("action",`/super-admin/`+$(this).attr('data-page')+`/`+$(this).attr('data-id')+`/delete`);
    });

 });
