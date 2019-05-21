import axios from 'axios'

export const get_list = () => {
    return axios
        .get('/api/todo', { headers: { "Content-type": "application/json" } })
        .then(res => {
            let data = []
            let todo_list = res.data.todo_list
            Object.keys(todo_list).forEach((key) => {
                let val = todo_list[key]
                data.push([val.id, val.work])
            })
            return data
        })
}

export const add_to_list = () => {
    return axios
    .get('')
}