$(window).on("load",function(){
  $("#computing_video").hide();
  $("#computing_type").on("change",function(){
    console.log(this.value);
    if(this.value == "Video"){
      console.log("video")
      $("#computing_image").hide();
      $("#computing_video").show();
    }else if(this.value == "Image"){
      $("#computing_image").show();
      $("#computing_video").hide();
    }
  })
})
