import axios from 'axios'

export const get_list = () => {
    return axios
        .get('/api/todo', { headers: { "Content-type": "application/json" } })
        .then(res => {
            let data = []
            let todo_list = res.data.todo_list
            Object.keys(todo_list).forEach((key) => {
                let val = todo_list[key]
                console.log(val)
                data.push([val.id, val.work, val.is_done])
            })
            console.log(data)
            return data
        })
}

export const add_to_list = todo_item => {
    return axios
        .post(
            '/api/todo',
            { work: todo_item },
            { headers: { "Content-type": "application/json" } }
        )
        .then(res => {
            console.log(res)
        })
}

export const delete_one = id => {
    return axios
        .delete(
            `/api/todo/${id}`
        )
        .then(res => {
            console.log(res)
        })
}

export const check_item = id => {
    return axios
        .put(
            `/api/todo/${id}`
        )
        .then(res => {
            console.log(res)
        })
}