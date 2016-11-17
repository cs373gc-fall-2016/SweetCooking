import React from 'react';
import $ from "jquery";

export default class SearchBox extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      message: '',
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleKeyUp = this.handleKeyUp.bind(this);
  }

  handleChange(event) {
    var that = this;
    var msg = event.target.value;
    this.setState({message: msg});
    if(this.state.message === ''){
      that.resetUI();
    }
  }

  handleKeyUp() {
    var that = this;
    if(this.state.message === ''){
      that.resetUI();
    }
    if($('.fa-spinner').length < 1) {
      $('#spinner').html('<i class="fa fa-spinner fa-pulse fa-4x fa-fw"></i>');
      $('#spinner').css("padding-top", "20px");
    }
    // console.log("this is outside: " + this.state.message);
    // run only once per search
    clearTimeout(window.timer);
    window.timer = setTimeout(function() {
      if(that.state.message !== '') {
        that.doSearch(that.state.message);
      }
      else {
        that.resetUI();
      }
    }, 1000);
  }

  
  resetUI() {
    $('#spinner').html('');
    $('#spinner').removeAttr('style');
    $('#search-and').html('');
    $('#search-or').html('');
  }

  render(){
    var message = this.state.message;
    return (
      <div className="input-group">
        <input type="text" className="form-control" value={message} onChange={this.handleChange} placeholder="Search for..." />
        <span className="input-group-btn">
          <a href={`/#/result/${message}`} className="btn btn-default">GO!</a>
        </span>
      </div>
    )
  }
}

