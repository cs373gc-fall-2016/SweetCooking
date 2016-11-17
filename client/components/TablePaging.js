import React from 'react';
import $ from "jquery";
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';

export default class TablePaging extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      products: [{
            id: 1,
            name: "Item name 1",
            price: 100
        },{
            id: 2,
            name: "Item name 2",
            price: 100
      }],
      searchPhrase: '',
    }
    console.log("before");
  }

  componentDidMount() {
    console.log("not con");
    this.setState ({
      searchPhrase: this.props.params.message,
    });
    this.doSearch(this.props.params.message);
  }

  doSearch(searchPhrase) {
    var that = this;
    // console.log("before ajax: " + searchPhrase);
    $.ajax({
      url: `/api/search/all?term=${searchPhrase}`,
      beforeSend: function() {
        // $('#search-and').html('<i class="fa fa-spinner fa-pulse fa-2x fa-fw"></i>');
      },
    }).done(function(data) {
      // that.resetUI();
      debugger;
      $('#search-and').append('<p>And :</p>');
      $('#search-or').append('<p>Or :</p>');
      
      that.searchDriver({
        data: data,
        searchType: 'and'
      });

      that.searchDriver({
        data: data,
        searchType: 'or'
      });

    });
 
  }

  searchDriver(args) {
    var that = this;

    var data = args.data;
    var searchType = args.searchType;


    var ingredientsHtml = '<ol class="ingredients-list"></ol>';
    var ingredientHtml = 'Ingredient';

    that.searchHelper({
      data: data,
      typeName: 'ingredients',
      searchType: searchType,
      elemHtml: ingredientHtml,
      elemsHtml: ingredientsHtml
    });

    var recipesHtml = '<ol class="recipes-list"></ol>';
    var recipeHtml = 'recipe';
    that.searchHelper({
      data: data,
      typeName: 'recipes',
      searchType: searchType,
      elemHtml: recipeHtml,
      elemsHtml: recipesHtml
    });

    var productsHtml = '<ol class="products-list"></ol>';
    var productHtml = 'product';
    that.searchHelper({
      data: data,
      typeName: 'products',
      searchType: searchType,
      elemHtml: productHtml,
      elemsHtml: productsHtml
    });

    var lifeStylesHtml = '<ol class="lifeStyles-list"></ol>';
    var lifeStyleHtml = 'lifeStyle';
    that.searchHelper({
      data: data,
      typeName: 'lifestyle',
      searchType: searchType,
      elemHtml: lifeStyleHtml,
      elemsHtml: lifeStylesHtml
    });
  }

  searchHelper(args) {
    var that = this;
    var data = args.data;
    var typeName = args.typeName;
    var searchType = args.searchType;
    var elemHtml = args.elemHtml;
    var elemsHtml = args.elemsHtml;

    if(searchType == 'and') {
      data = data['and'][typeName]; 

      that.searchDataProcess({
        data: data,
        typeName: typeName,
        searchType: searchType,
        elemHtml: elemHtml,
        elemsHtml: elemsHtml
      });
    } else {
      data = data['or'][typeName];
      var keys = Object.keys(data);

      $.each(keys, function(index, key) {
        var temp = data[key];
        // debugger
        that.searchDataProcess({
          data: temp,
          typeName: typeName,
          key: key,
          searchType: searchType,
          elemHtml: elemHtml,
          elemsHtml: elemsHtml
        });
      });
    }
  }

  searchDataProcess(args) {
    var that = this;
    var data = args.data;
    var typeName = args.typeName;
    var searchType = args.searchType;
    var key = args.key;
    var elemHtml = args.elemHtml;
    var elemsHtml = args.elemsHtml;

    if(data.length > 0) {
      if(searchType == 'or') {
        elemHtml = key;
      }
      data = data.slice(0,3);
      $(data).each(function(i, ele){
        elemHtml += `<li><a href="/${typeName}/${ele.id}">${ele.name}</a></li>`;
      });

      if(searchType == 'or') {
        if($(`#search-${searchType} .${typeName}-list`).length < 1) {
          $(`#search-${searchType}`).append(`<p style="text-transform: capitalize">${typeName}</p>`).append(elemsHtml);
        }
        var title = `<ol class="${key}">${key}</ol>`;
        $(`#search-${searchType} .${typeName}-list`).append(title);
        $(`#search-${searchType} .${typeName}-list .${key}`).html(elemHtml);
      } else {
        if($(`#search-${searchType} .${typeName}-list`).length < 1) {
          $(`#search-${searchType}`).append(elemsHtml);
        }
        $(`#search-${searchType} .${typeName}-list`).html(elemHtml);
      }
    }
  }


  render() {
    var searchPhrase = this.state.searchPhrase;
    var products = this.state.products;
    return (
      <BootstrapTable data={products} striped={true} hover={true}>
        <TableHeaderColumn dataField="id" isKey={true} dataAlign="center" dataSort={true}>Product ID</TableHeaderColumn>
        <TableHeaderColumn dataField="name" dataSort={true}>Product Name</TableHeaderColumn>
        <TableHeaderColumn dataField="price" dataFormat={this.priceFormatter}>Product Price</TableHeaderColumn>
      </BootstrapTable>
    )
  }
}

