import React, { useState, useEffect} from 'react'

import { getCookie } from '../../app/csrf'
import style from './AddForm.css'

export default function AddForm(props) {
    /*
        The form required list of input the inputs will be in the following
        name:
        label_message:
        type:
        options: (optional for categories and shit)
        placeholder:
        size_of_padding
    */

    let { url } = props
    let { form } = props
    const keys = form.form.map((structure)=>structure.name)
    let form_structure = form.form.map((structure, key) =>
            <div key={key} className="form_input" style={{padding: structure.size_of_padding}}>
                <label htmlFor={structure.name}>{structure.label_message}</label>
                <input type={structure.type} id={structure.name} placeholder={structure.placeholder}/>
            </div>
        
        )
    let handleSubmit = function(e){
        const target = e.target
        const values = []
        const body = {}
        for( let i = 0 ; i < keys.length; i++){
            body[keys[i]] = target[keys[i]].value
        }
        const csrf = getCookie('csrftoken')
        console.log(`body ${JSON.stringify(body)}`);
        const request = {
            method: 'POST',
            body: JSON.stringify(body),
            headers: {
                'X-CSRFToken': csrf,
                'Content-Type': 'application/json'
            }
        }
        fetch(url, request)
            .then(data=> data.json())
            .then(data => {
                console.log(data)
            })
            .catch(err =>{
                console.log('ERR')
                console.log(err)
            })
        e.preventDefault()
    }
    return (
        <div className="add_form">
            <div className="add_form_header" onClick={()=> props.hide()}>
                X
            </div>
            <div className="add_form_body">
                <form action="" method="post" onSubmit={handleSubmit}>
                    {form_structure}
                    <input type="submit" value="Submit"/>
                </form>
            </div>
        </div>
    )
}
