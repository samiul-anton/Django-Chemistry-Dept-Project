$(document).ready(function () {
  //Load more fucnction
     $(".span9 article").hide();
     size_li = $(".span9 article").size();
     console.log(size_li);
     x=2;
     $(`.span9 article:lt(`+x+`)`).show();
     if(size_li == x){
       $("#loadMore").hide();
     }else{
       $('#loadMore').click(function () {
           x= (x+5 <= size_li) ? x+5 : size_li;
           if(size_li == x){
             $("#loadMore").hide();
           }
           $('.span9 article:lt('+x+')').show();
       });

     }

});
