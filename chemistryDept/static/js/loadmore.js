$(document).ready(function () {
  //Load more fucnction
   function load_more(list){
     size_li = $(list).size();
     x=3;
     $(list:lt('+x+')').show();
     $('#loadMore').click(function () {
         x= (x+5 <= size_li) ? x+5 : size_li;
         $('list:lt('+x+')').show();
     });
   }

});
