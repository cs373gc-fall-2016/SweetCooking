import routes from './config/routes';
import React from 'react';
import ReactDOM from 'react-dom';

var ServiceChooser = React.createClass({
    render: function() {
        return 
        <div>
            <h1>Our services</h1>
        </div>
    }

});

ReactDOM.render(
    routes,
    document.getElementById('search-box')
);