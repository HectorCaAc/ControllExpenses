import React, { useState } from "react";
import { render } from 'react-dom';

import { get_categories, get_category } from '../api/RESTCategory'

function Categories(props){

    
    const makeRequest= ()=>{
        console.log('The button was plessed to make more request')
        get_categories('TEST')    
    }

    const makeSecondRequest = () =>{
        console.log('modifying the type of the fetch')
        get_category('TEST', 'GAS')
    }
    return(
        <div >
            <h4>Make request for the categories</h4>
            <h3>Lets try to use a button that when click will make the request</h3>
            <h3>Lets this work with webpack and redux, let build this app and deploy it to the real wolrd
            </h3>
            <div className="button" onClick={makeRequest}>MAKE request</div>
            <div className="button" onClick={makeSecondRequest}>SECOND TEST</div>
        </div>
    )
}

export default Categories;

const container = document.getElementById('category_pannel');
render(<Categories />, container);