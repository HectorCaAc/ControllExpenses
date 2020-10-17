import React, { useState, useEffect } from "react"
import { useSelector } from 'react-redux'
import { useDispatch } from 'react-redux'


import style from './category.css'
import LeftPannel from './leftPannel'
import { get_category } from '../../api/RESTCategory'
import { setUser } from './categorySlice'

function Category(props) {
    const currentCategory = useSelector(state => state.category)
    if (currentCategory.user === ''){
        const dispatch = useDispatch()
        dispatch(setUser(props.name))
    }
    return (
        <div className="category">
            <div className="category_options">
                <LeftPannel name={props.name} />
            </div>
            <div className="category_body">
                <div className="category_body_header">
                    <div className="header_item">
                        <h2>{currentCategory.category}</h2>
                    </div>
                    <div className="category_body_options">
                        <div className="body_options">Introduction</div>
                        <div className="body_options">Modify</div>
                        <div className="body_options">Export</div>
                    </div>
                </div>
                <CategoryBody />
            </div>
        </div>
    )
}

function CategoryBody() {
    // Get data from the body
    // required to have the category and the user
    const currentCategory = useSelector(state => state.category)
    // for now just get that category and make the request
    const [categoryDisplay, setCategory] = useState({
        loading: true,
        data: {}
    })

    console.log('data from CategoryBody')
    console.log(currentCategory)
    useEffect(() => {
        console.log('Categorybody was request to change...');
        if (currentCategory.category !== '' && currentCategory.user !== '') {
            let category = get_category(currentCategory.user, currentCategory.category)
            category.then(data => {
                let rows = <div className="category_display_data">
                    <div><h4>spend_available </h4><div>{data.data.spend_available}</div></div>
                    <div><h4>current_circle </h4><div>{data.data.current_circle}</div></div>
                    <div><h4>expense </h4><div>{data.data.expense}</div></div>
                    <div><h4>deficit ? </h4><div>{data.data.deficit ? 'Yes': 'No'}</div></div>
                    <div><h4>circle_repetition </h4><div>{data.data.circle_repetition} </div></div>
                </div>
                setCategory({ loading: false, data: rows })
            })
        }
}, [currentCategory, setCategory])

return (
    <div className="category_display">
        {categoryDisplay.loading &&
            <h2>Select a Category</h2>
        }
        {!categoryDisplay.loading &&
            categoryDisplay.data
        }

    </div>
)

}

export default Category;