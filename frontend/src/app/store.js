import { configureStore } from '@reduxjs/toolkit'

import categoryReducer from '../components/Category/categorySlice'
// Things that should be save in the store

// name of the category
// the data coming from back end
// In the future I would like to be able to store multiple categories, 
// but for now only store one
// The name of the user

export default configureStore({
    reducer:{
        category: categoryReducer
    }
})