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

function add_entry(data){
  send_post('/api/expenses/add/', data);
}

function create_income(){

}

function delete_category(category_id){
  let url = '/api/category/delete/';
  let data={
    id_category: category_id
  };
  send_post(url, data);
}

function delete_entries(ids){
  let url='/api/expenses/delete/';
  let data={
    expenses_id: ids
  }
  send_post(url, data);
}

function delete_income(){

}

function send_post(url, data){
  console.log(url);
  let csrf = getCookie('csrftoken');
  fetch(url,{
    method:"POST",
    credentials:"same-origin",
    headers:{
      "X-CSRFToken":csrf,
      "Accept":"application/json",
      "Content-Type":"application/json"
    },
    body: JSON.stringify(data)
  }).then((response)=>{
    console.log(response);
    return response.json()
  }).then((response)=>{
    console.log(response);
  }).catch((response)=>{
    console.log(response);
  })
}
export {delete_category,
        add_entry,
        delete_entries}
