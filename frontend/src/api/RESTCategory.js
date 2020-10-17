
const base_url = 'http://localhost:8000/api/'

async function get_categories(user){
    let url = `${base_url}category/${user}/`
    console.log(`Api request for user:  ${user}`);
    const data = await fetch(url)
            .then(data=>data.json())
    return data
}

async function get_category(user, category_name){
    let url = `${base_url}category/${user}/${category_name}/`
    console.log(`Getting data for user ${user} and the category ${category_name}`)
    const response = await fetch(url,{
                    headers:{
                        'accepts':'application/json'
                    }
                })
                .then(data=> {
                    console.log(data)
                    return data.json()
                })
                .catch((error)=> {
                    console.log('There was an error loading the data')
                    console.log(error)
                })
    return response
}

module.exports ={
    get_categories, 
    get_category
}