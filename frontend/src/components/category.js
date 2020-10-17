import style from './category.css'

import React, { useState, useEffect } from "react";
import { render } from 'react-dom';

import { get_categories, get_category } from '../api/RESTCategory'

function Category(props) {
    return (
        <div className="category">
            <div className="category_options">
                <LeftPannel name={props.name} />
            </div>
            <div className="category_body">
                <div className="category_body_header">
                    <div className="header_item">
                        CATEGORY NAME HERE
                    </div>
                    <div className="category_body_options">
                        <div className="body_options">Introduction</div>
                        <div className="body_options">Modify</div>
                        <div className="body_options">Export</div>
                    </div>
                </div>
            </div>
        </div>
    )
}

function LeftPannel(props) {
    console.log('The username is being passed from the html tag to the parent object to this object CHANGE THAT ASS SOON AS POSSIBLE');
    let [dataState, setAppState] = useState({
        loading: true,
        categories: []
    })

    useEffect(() => {
        let data = get_categories(props.name)
        data.then(input => {
            let categories_rows = input.categories.map((entry, key) =>
                <div className="left_pannel_category" key ={key}>
                    <div className="category_name">{entry.name}</div>
                    <div className="category_data">
                        <div className="category_data_expense">
                            <h4>Category Expense</h4>
                            {entry.expense}
                            <h4>Current Expense</h4>
                            {entry.spend_available}
                        </div>
                    </div>
                </div>
                )
            setAppState({loading: false, categories: categories_rows})
        })
    }, [setAppState])
    
    
    return (
                <div className="left_pannel">
                    { dataState.loading &&
                        <h2>Loading Data</h2>
                    }
                    {
                        !dataState.loading &&
                        dataState.categories
                    }
                </div>
            )

        }

export default Category;

const container = document.getElementById('category_pannel');
render(<Category name={container.getAttribute('name')} />, container);