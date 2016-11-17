import React from 'react';
import $ from "jquery";
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';

export default class TablePaging extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      searchPhrase: '',
      searchRe: [
        {ingredient_name: 'a',
         recipe_name: 'b',
         product_name: 'c',
         lifestyle_name: 'd'},
        {ingredient_name: 'e',
         recipe_name: 'f',
         product_name: 'g',
         lifestyle_name: 'h'}
      ],
    }
  }

  componentDidMount() {
    var searchPhrase = this.state.searchPhrase;
    searchPhrase = this.props.params.message
    this.setState ({
      searchPhrase: searchPhrase,
    });

    this.doSearch(searchPhrase);
  }

  doSearch(searchPhrase) {
    var that = this;
    var searchRe = this.state.searchRe;
    // console.log("before ajax: " + searchPhrase);
    $.ajax({
      url: `/api/search/all?term=${searchPhrase}`,
      beforeSend: function() {
        // $('#search-and').html('<i class="fa fa-spinner fa-pulse fa-2x fa-fw"></i>');
      },
    }).done(function(data) {
      // that.resetUI();

      $('#search-and').append('<p>And :</p>');
      $('#search-or').append('<p>Or :</p>');
      
      that.searchDriver({
        data: data,
        searchType: 'and',
        searchP: searchPhrase
      });

      that.searchDriver({
        data: data,
        searchType: 'or',
        searchP: searchPhrase
      });
    });
  }

  searchDriver(args) {
    var that = this;

    var data = args.data;
    var searchType = args.searchType;
    var searchP = args.searchP;

    var ingredientsHtml = '<ol class="ingredients-list"></ol>';
    var ingredientHtml = 'Ingredient';

    that.searchHelper({
      data: data,
      typeName: 'ingredients',
      searchP: searchP,
      searchType: searchType,
      elemHtml: ingredientHtml,
      elemsHtml: ingredientsHtml
    });

    var recipesHtml = '<ol class="recipes-list"></ol>';
    var recipeHtml = 'recipe';
    that.searchHelper({
      data: data,
      typeName: 'recipes',
      searchP: searchP,
      searchType: searchType,
      elemHtml: recipeHtml,
      elemsHtml: recipesHtml
    });

    var productsHtml = '<ol class="products-list"></ol>';
    var productHtml = 'product';
    that.searchHelper({
      data: data,
      typeName: 'products',
      searchP: searchP,
      searchType: searchType,
      elemHtml: productHtml,
      elemsHtml: productsHtml
    });

    var lifeStylesHtml = '<ol class="lifeStyles-list"></ol>';
    var lifeStyleHtml = 'lifeStyle';
    that.searchHelper({
      data: data,
      typeName: 'lifestyle',
      searchP: searchP,
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
    var searchP = args.searchP;


    if(searchType == 'and') {
      data = data['and'][typeName]; 

      that.searchDataProcess({
        data: data,
        typeName: typeName,
        searchP: searchP,
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
          searchP: searchP,
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
    var searchP = args.searchP;
    var searchType = args.searchType;
    var key = args.key;
    var elemHtml = args.elemHtml;
    var elemsHtml = args.elemsHtml;

    if(data.length > 0) {
      if(searchType == 'or') {
        elemHtml = key;
      }      
      
      console.log(that);
      console.log(searchP);
      data = data.slice(0,10);
      $.each(data, function(i, ele){
        // debugger
        if(ele.name.indexOf("beef") > 0) {
          var x = ele.name.split("beef");
        } else {
          var x = ele.name.split("Beef");
        }
        // debugger
        elemHtml += `<li><a href="/${typeName}/${ele.id}">${x[0]}<span style="background-color: yellow;">beef</span>${x[1]}</a></li>`;
        
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
    var searchRe = this.state.searchRe;
    return (
      <BootstrapTable data={searchRe} pagination={true}>
        <TableHeaderColumn dataField="ingredient_name" isKey={true} dataAlign="center" dataSort={true}>Ingredients</TableHeaderColumn>
        <TableHeaderColumn dataField="recipe_name" dataAlign="center" dataSort={true}>Recipes</TableHeaderColumn>
        <TableHeaderColumn dataField="product_name" dataAlign="center" dataSort={true}>Products</TableHeaderColumn>
        <TableHeaderColumn dataField="lifestyle_name" dataAlign="center" dataSort={true}>Lifestyles</TableHeaderColumn>
      </BootstrapTable>
    )
  }
}

