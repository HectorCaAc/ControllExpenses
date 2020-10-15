import { createSlice } from '@reduxjs/toolkit'

const categorySlice = createSlice({
    name: 'categories',
    initialState: {
        index: 0
    },
    reducers: {
        selectNew: state =>{
            // reducer that will change the index, and one of the children will 
            // take of that and make the right api callss for that
        }
    }

})