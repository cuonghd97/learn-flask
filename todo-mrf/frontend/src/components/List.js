import React, { Component } from 'react'

import { get_list } from '../ListFunctions'

class List extends Component {
    constructor() {
        super()

        this.state = {
            id: '',
            work: '',
            isEdit: false,
            todo_items: []
        }
    }

    componentDidMount() {
        this.getAll()
    }

    getAll = () => {
        get_list().then(data => {
            this.setState({
                todo_items: [...data]
            })
        })
    }

    render() {
        const { todo_items } = this.state
        return(
            <div>
                <div>
                    <input type="text" name="work" id="work"/>
                    <button>Add</button>
                </div>
                {
                    todo_items.map((item, index) => {
                        return <p key={index}>{item[1]}</p>
                    })
                }
            </div>
        )
    }
}

export default List