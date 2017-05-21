import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
// import './index.css';

// ReactDOM.render(<App />, document.getElementById('root'));

var data  = [
  {"id": 1, "author": "alice", "text": "I'm alice"},
  {"id": 2, "author": "bob", "text": "I'm bob"},
]

class CommentBox extends React.Component{
  render(){
    return(
      <div className="commentBox">
        <h1>commentBox</h1>
        {this.props.message}
        {this.props.hoge}
      </div>
    )
  }
}

ReactDOM.render(
  <CommentBox message={"hello, world REACT"} hoge={"hogehoge"}/>,
  document.getElementById('root')
);

// registerServiceWorker();
