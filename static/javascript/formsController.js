import {add_entry, add_income} from './api.js';

function serialized_to_json(serialized_data){
    let split = serialized_data.split('&');
    let data = split.reduce((o, key)=>{
        let keys_split = key.split('=');
        return ({
            ...o, [keys_split[0]]: keys_split[1]
        })},{});
    console.log('from serialized to object success');
    return data
};

$('#form-income').submit((e)=>{
    e.preventDefault();
    let currentForm= $(e.currentTarget).serialize();
    let data = serialized_to_json(currentForm);
    console.log("income add");
    add_income(data);
})
function entry_form(data){


};

function income_form(data){

};

export {
    entry_form,
    income_form
};

