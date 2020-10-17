import { createSlice } from '@reduxjs/toolkit'

export const categorySlice = createSlice({
    name: 'category',
    initialState: {
        category: ""
    },
    reducers:{
        selected: (state, action) =>{
            state.currentCategory =action.payload 
        },
        
    }
})

export const {selected} = categorySlice.actions

export default categorySlice.reducer