import React, { Component } from 'react';
import './App.css';

class App extends Component {

  state = {count: 0}

  countUp = e => {
    e.preventDefault()
    console.log('countup')
    fetch('/api/count', {
      method: 'POST',
      body: 'up'
    }).then(res => {
      if (res.ok) {
        this.setState({count:
          {count: this.state.count.count + 1}
        })
      }
    })
  }

  countDown = e => {
    e.preventDefault()
    console.log('countdown')
    fetch('/api/count', {
      method: 'POST',
      body: 'down'
    }).then(res => {
      if (res.ok) {
        this.setState({count:
          {count: this.state.count.count - 1}
        })
      }
    })
  }

  loadCountFromServer = () => {
    fetch('/api/count')
      .then(res => {
        if (!res.ok) {
          throw Error(res.statusText)
        }
        return res.json()
      })
      .then(count => this.setState({count: count }));
  }

  componentDidMount() {
    this.loadCountFromServer()
    setInterval(this.loadCountFromServer, 1000)
  }

  render() {
    return (
      <div className="App">
        <Header />
        <Counter count={this.state.count} countUp={this.countUp}
        countDown={this.countDown}/>
      </div>
    );
  }
}

class Header extends Component {
  render(){
    return (
      <div className="App-header">
        <h2>Counter App</h2>
      </div>
    )
  }
}

class Counter extends Component {
  render(){
    return (
      <div className="counter">
        {/*<p>{this.state.comments.map(comment =>*/}
        {/*<div key={comment.id}>{comment.author}</div>*/}
        {/*)}</p>*/}
        <p>{this.props.count.count}</p>
        <form onSubmit={this.props.countUp} >
          <input type="submit" value="+" />
        </form>
        <form onSubmit={this.props.countDown} >
          <input type="submit" value="-" />
        </form>
      </div>
    )
  }
}

export default App;
