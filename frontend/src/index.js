import "@babel/polyfill"

import React from 'react'
import Category from './components/Category/category';
import { Provider } from 'react-redux'
import { render } from 'react-dom'

import store from './app/store'

const container = document.getElementById('category_pannel');
render(
    <Provider store={store}>
        <Category name={container.getAttribute('name')} />
    </Provider>
    , container);