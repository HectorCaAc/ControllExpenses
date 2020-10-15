import React, { useState } from "react";
import { render } from 'react-dom';


function Categories(props){
    return(
        <div >
            <h5>Category selected</h5>
        </div>
    )
}

export default Categories;

const container = document.getElementById('category_pannel');
render(<Categories />, container);

