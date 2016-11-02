import React from 'react';
import searchBox from '../components/searchBox';
import {Router, Route, IndexRoute, hashHistory} from 'react-router';

var Main = React.createClass({
  render: function() {
    return (
      <div>
        <h1> HHHHHHHHHHHH </h1>
      </div>
    )
  }
});

var Home = React.createClass({
  render: function() {
    return (
      <div>
        <h1>Hello there</h1>
      </div>
    )
  }
});


var ViewContainer = React.createClass({
  render: function() {
    return (
      <h1> LLLLLLLLLLLLL </h1>
    )
  }
});

var routes = (
  <Router history={hashHistory}>
    <Route path='/' component={searchBox}>
      <IndexRoute component={Home} />
      <Route path='view' component={ViewContainer} />
    </Route>
  </Router>
);

module.exports = routes;
