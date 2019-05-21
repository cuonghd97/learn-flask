import React, { Component } from 'react'
import classNames from 'classnames/bind'
import { get_list, add_to_list, delete_one, check_item } from '../ListFunctions'

import './List.css'

class List extends Component {
    constructor() {
        super()

        this.state = {
            id: '',
            work: '',
            isEdit: false,
            todo_items: [],
        }

        this.onChange = this.onChange.bind(this)
        this.removeItem = this.removeItem.bind(this)
        this.checkItem = this.checkItem.bind(this)
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

    onChange = e => {
        this.setState({
            work: e.target.value
        })
    }

    onSubmit = e => {
        e.preventDefault()
        add_to_list(this.state.work).then(
            () => {
                this.getAll()
            }
        )
    }

    removeItem(item) {
        return event => {
            delete_one(item[0])
                .then(() => {
                    this.getAll()
                })
        }
    }

    checkItem(item) {
        return event => {
            check_item(item[0])
                .then(() => {
                    this.getAll()
                })
        }
    }

    render() {
        const { todo_items } = this.state
        console.log(todo_items)
        return(
            <div>
                <div>
                    <form>
                        <input
                            type="text"
                            name="work"
                            id="work"
                            defaultValue={this.state.work}
                            onChange={this.onChange}
                        />
                        <button onClick={this.onSubmit}>Add</button>
                    </form>
                </div>
                <div className="todolist">
                {
                    todo_items.map((item, index) => {
                        return (
                            <p
                                key={index}
                                className={classNames({
                                    'done': item[2] !== 0
                            })}>
                                <button onClick={this.checkItem(item)}>0</button>
                                {item[1]}
                                <button onClick={this.removeItem(item)}>remove</button>
                            </p>
                        )
                    })
                }
                </div>
            </div>
        )
    }
}

export default List