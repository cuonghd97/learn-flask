import React, { Component } from "react"
import ReactDOM from "react-dom"
import axios from "axios"
import { notify } from "react-notify-toast"
// axios.defaults.headers.post['Content-Type'] ='application/x-www-form-urlencoded';
class App extends Component {
    constructor() {
        super()

        this.state = {
            username: '',
            password: ''
        }

        this.changeValue = this.changeValue.bind(this)
    }
    login = (username, password) => {
        return axios
            .post(
                "http://192.168.40.225:5000/login",
                {
                    "username": username,
                    "password": password
                },
                { headers: { "Content-type": "application/json" } }
            )
            .then(res => {
                console.log(res.data.access_token)
                localStorage.setItem("access_token", res.data.access_token)
            })
    }

    handleFormSubmit = (e) => {
        e.preventDefault()
        this.login(this.state.username, this.state.password)
    }

    changeValue = (event) => {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    render() {
        console.log(this.state)
        return(
            <div>
                <h1>Hello world</h1>
                <form method="post">
                    <input
                        type="text"
                        name="username"
                        id="username"
                        placeholder="username"
                        onChange={this.changeValue}
                    />
                    <input
                        type="password"
                        name="password"
                        id="password"
                        onChange={this.changeValue}
                    />
                    <button onClick={this.handleFormSubmit}>Login</button>
                </form>
            </div>
        )
    }
}
export default App

ReactDOM.render(<App/>, document.getElementById("root"))