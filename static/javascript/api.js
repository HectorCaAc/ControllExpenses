/*
  It will required to use jquery
*/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function create_category (){
}

function create_entry(){
  console.log("Create_entry");
}

function create_income(){

}

function delete_category(category_id){
  let url = '/api/expenses/delete/';
  let csrf = getCookie('csrftoken');
  let data={
    id_category: category_id
  }
  fetch(url,{
    method:"POST",
    credentials:"same-origin",
    headers:{
      "X-CSRFToken":csrf,
      "Accept":"application/json",
      "Content-Type":"application/json"
    },
    body: JSON.stringify(data)
  }).then((response)=>
      response.json()
  ).then((response)=>{
    console.log(response);
  }).catch((response)=>{
    console.log(response);
  })
}

function delete_entries(ids){
  console.log("entries that are going to delete");
  console.log(ids);
}

function delete_income(){

}

export {delete_category, create_entry}
