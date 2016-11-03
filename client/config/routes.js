import React from 'react';
import ReactDOM from 'react-dom';
import searchBox from '../components/searchBox';
import {Router, Route, IndexRoute, hashHistory} from 'react-router';

var Main = React.createClass({
  render: function() {
    return (
      <div>
        <h1> Hello People </h1>
      </div>
    )
  }
});


var Hello = React.createClass({
 render: function() {
    return (
      <div> Hello World </div>
    )
  }
});


var ViewContainer = React.createClass({
  render: function() {
    return (
      <h1> Hello YOYOYOYYO </h1>
    )
  }
});

var routes = (
  <Router history={hashHistory}>
    <Route path='/' component={searchBox}>
      <IndexRoute component={Hello} />
      <Route path='view' component={ViewContainer} />
    </Route>
  </Router>
);

module.exports = routes;
