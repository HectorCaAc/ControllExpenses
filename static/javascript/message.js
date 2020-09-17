import {delete_category, delete_entries} from './api.js'


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

$('.action').click((e)=>{
  let modalSelect = $(e.currentTarget).attr('modal-data');
  $(`#modal-${modalSelect}`).show();
  $(`#modal-${modalSelect}`).animate({opacity:1}, 1250);
});

$('.close_modal').click((e)=>{
  let modal_choose =$(e.currentTarget).attr('modal') ;
  console.log(`try to close modal ${modal_choose}`);
  $(`#modal-${modal_choose}`).animate({opacity:0}, 1000);
  $(`#modal-${modal_choose}`).hide();
});

$(document).ready(()=>{
  $(".delete-target").click((event)=>{
      let id = event.target.getAttribute("data-id");
      let name = event.target.getAttribute("data-name")
      $('#delete_entries').data('id',id);
      $('#delete-entries').modal('show');
      $('#modal-category').append(name+'"');
  });
});

function adjust_balance(rows_array){
  let amount = rows_array.map(entry=>{
    return parseFloat(entry.cells[2].innerHTML,10)
  });
  amount = amount.reduce((total, value)=>total+value);
  let current_valance = $('#current_balance').html().substr(2);
  current_valance = parseFloat(current_valance);
  current_valance += amount;
  $('#current_balance').html("$ "+current_valance.toFixed(2));
}

function get_entries_ids(rows){
  console.log("get_entries");
  let ids = rows.map((entry)=>entry.getAttribute("data-expense-id"))
  return ids;
}

$("#delete_category").click(()=>{
  let category_id = $('#delete_entries').data('id');
  let delete_all_entries = $('#delete_entries').is(":checked");
  fade_and_remove("tr[data-row-id='"+category_id+"']");
  if(delete_all_entries){
    let all_categories = "tr[data-category-id = '"+category_id+"']";
    let array = Object.values($(all_categories)).slice(0,-2);
    let entries_id = get_entries_ids(array);
    adjust_balance(array);
    fade_and_remove(all_categories);
    delete_entries(entries_id);
  }
  delete_category(category_id);
  $('#delete-entries').modal('hide');
});

$('#cancell_category').click(()=>{
  $('#delete-entries').modal('hide');
})

