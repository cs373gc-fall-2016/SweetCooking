import React from 'react';
import ReactDOM from 'react-dom';
import SearchBox from '../components/SearchBox';
import TablePaging from '../components/TablePaging';
import {Router, Route, IndexRoute, hashHistory} from 'react-router';


var routes = (
  <Router history={hashHistory}>
    <Route path='/' component={SearchBox}></Route>
    <Route path='/result/:message' component={TablePaging}></Route>
    
  </Router>
);

module.exports = routes;
