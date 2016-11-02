var ServiceChooser = React.createClass({
    render: function() {
        return 
        "<div>
            <h1>Our services</h1>
            
            <div id="services">
                <p id="total">Total</p>

            </div>
        </div>"
    }

});

ReactDOM.render(
    <ServiceChooser/>,
    document.getElementById('sort-table')
);