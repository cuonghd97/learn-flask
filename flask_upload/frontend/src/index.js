import React, { Component } from "react"
import ReactDOM from "react-dom"
import axios from "axios"
axios.defaults.headers.post['Content-Type'] ='application/x-www-form-urlencoded';
class App extends Component {
    login = () => {
        return axios
            .post(
                "http://192.168.40.225:5000/login",
                {
                    "username": "cuong1",
                    "password": "1"
                },
                { headers: { "Content-type": "application/json" } }
            )
            .then(res => {
                console.log(res)
            })
    }

    componentDidMount() {
    }

    click = () => {
        console.log("click")
        this.login()
    }

    render() {
        return(
            <div>
                <h1>Hello world</h1>
                <button onClick={this.click}>Click</button>
            </div>
        )
    }
}
export default App

ReactDOM.render(<App/>, document.getElementById("root"))