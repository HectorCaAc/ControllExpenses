import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    'user': '',
    'category': ''
}

export const categorySlice = createSlice({
    name: 'category',
    initialState,
    reducers:{
        selected: (state, action) =>{
            console.log('Data recerived in the reducer');
            state.category =action.payload 
        },
        setUser: (state, action)=>{
            state.user = action.payload
        }
        
    }
})

export const {selected, setUser} = categorySlice.actions

export default categorySlice.reducer