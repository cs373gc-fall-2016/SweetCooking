import routes from './config/routes';
import React from 'react';
import ReactDOM from 'react-dom';
import TablePaging from './components/TablePaging';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';


ReactDOM.render(
    routes,
    document.getElementById('search-box')
);
