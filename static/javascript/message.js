import {delete_category, create_entry} from './api.js'

console.log("The UI should be the last thing");
console.log("be sure that if the categoreis is to long just show certain amount of it");
console.log("Also javascript should be use to arrage elements");
console.log("one fo the things is import just the api, it will be more human readable");

function fade_and_remove(jquery_expresion){
  let road_select = $(jquery_expresion);
  road_select.animate({
      opacity:"0"
  },1000,()=>road_select.hide());
}

/*
  It will required to add the end points for the
  api and that is
  and then the celery thing
  
*/
$(document).ready(()=>{
  $(".delete-target").click((event)=>{
      let id = event.target.getAttribute("data-id");
      let name = event.target.getAttribute("data-name")
      $('#delete_entries').data('id',id);
      $('#delete-entries').modal('show');
      $('#modal-category').append(name+'"');
  });
});

function remove_entries(category_pk){
  let all_categories = "tr[data-category-id = '"+category_pk+"']";
  console.log("all categories");
  console.log($(all_categories));
  let array = Object.values($(all_categories)).slice(0,-2);
  let amount = array.map(entry=>{
    console.log(entry.cells[2].innerHTML);
    return parseFloat(entry.cells[2].innerHTML,10)
  });
  console.log(amount);
  amount = amount.reduce((total, value)=>total+value);
  let current_valance = $('#current_balance').html().substr(2);
  current_valance = parseFloat(current_valance);
  console.log("current valance "+current_valance);
  current_valance += amount;
  console.log("amount of the category "+amount);
  $('#current_balance').html("$ "+current_valance.toFixed(2));
  fade_and_remove(all_categories);
}

$("#delete_category").click(()=>{
  let category_id = $('#delete_entries').data('id');
  let delete_all_entries = $('#delete_entries').is(":checked");
  fade_and_remove("tr[data-row-id='"+category_id+"']");
  delete_category(category_id);
  if(delete_all_entries){
    remove_entries(category_id);
  }
  $('#delete-entries').modal('hide');
});

$('#cancell_category').click(()=>{
  $('#delete-entries').modal('hide');
})
