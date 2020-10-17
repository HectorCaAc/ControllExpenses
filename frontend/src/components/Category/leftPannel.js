import style from './leftPannel.css'
import React, { useState, useEffect } from 'react'
import { useDispatch } from 'react-redux'

import { get_categories } from '../../api/RESTCategory'
import { selected } from './categorySlice'


// Send data to the redux object
// I don't need the props anymore I could just start to use redux to solve all my problems
function LeftPannel(props) {
    console.log('The username is being passed from the html tag to the parent object to this object CHANGE THAT ASS SOON AS POSSIBLE');
    const [dataState, setAppState] = useState({
        loading: true,
        categories: []
    })

    const dispath = useDispatch()

    const new_category = (category_name) =>{
        console.log(`Category [${category_name}] selected`);
        dispath( selected(category_name))
    }

    useEffect(() => {
        let data = get_categories(props.name)
        data.then(input => {
            let categories_rows = input.categories.map((entry, key) =>
                <div className="left_pannel_category" key={key}
                    onClick={()=> new_category(entry.name)}
                >
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
            setAppState({ loading: false, categories: categories_rows })
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

export default LeftPannel