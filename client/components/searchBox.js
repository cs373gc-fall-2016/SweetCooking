import React from 'react';

var searchBox = React.createClass({
  getInitialState: function() {
    return{
      message: '',
    }
  },

  handleChange: function(event) {
    this.setState({message: event.target.value});
    console.log(this.state.message);
    this.doSearch();
  },

  doSearch: function() {
    $.get(url)
    console.log(this.state.message);  
  },

  render:function(){
    var message = this.state.message;
    return (
      <div className="input-group">
        <input type="text" className="form-control" value={message} onChange={this.handleChange} placeholder="Search for..." />
        <span className="input-group-btn">
          <button className="btn btn-default" type="button">Go!</button>
        </span>
      </div>
    )
  }
});

module.exports = searchBox;