import routes from './config/routes';
import React from 'react';
import ReactDOM from 'react-dom';

var Hello = React.createClass({
 render: function() {
    return (
      <div> Anyway, Hello World </div>
    )
  }
});

ReactDOM.render(
    routes,
    document.getElementById('search-box')
);
