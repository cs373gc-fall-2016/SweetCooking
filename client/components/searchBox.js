import React from 'react';
import $ from "jquery";

var searchBox = React.createClass({
  getInitialState: function() {
    return {
      message: '',
    }
  },

  handleChange: function(event) {
    var that = this;
    var msg = event.target.value;
    this.setState({message: msg});
    if(this.state.message === ''){
      $('#search-and').html('');
    }
    // console.log("testing: " + this.state.message);

  },

  handleKeyUp: function() {
    var that = this;
    if(this.state.message === ''){
      $('#search-and').html('');
    }
    if($('.fa-spinner').length < 1) {
      $('#search-and').html('<i class="fa fa-spinner fa-pulse fa-2x fa-fw"></i>');
    }
    // console.log("this is outside: " + this.state.message);
    // run only once per search
    clearTimeout(window.timer);
    window.timer = setTimeout(function() {
      if(that.state.message !== '') {
      // console.log(that.state.message);
        that.doSearch(that.state.message);
      }
      else {
        $('#search-and').html('');
      }
    }, 1000);
  },

  doSearch: function(searchPhrase) {
    var that = this;
    // debugger;
    // console.log("before ajax: " + searchPhrase);
    $.ajax({
      url: `/api/search/all?term=${searchPhrase}`,
      beforeSend: function() {
        // $('#search-and').html('<i class="fa fa-spinner fa-pulse fa-2x fa-fw"></i>');
      },
    }).done(function(data) {
      // debugger;
      // console.log("ajax finished: " );
      $('#search-and').html('');
      var ingredientsHtml = '<ol id="ingredients-list"></ol>';
      var ingredientHtml = 'Ingredient';
      that.searchHelper({
        data: data,
        typeName: 'ingredients',
        elemHtml: ingredientHtml,
        elemsHtml: ingredientsHtml,
        searchName: 'and'
      });

      var recipesHtml = '<ol id="recipes-list"></ol>';
      var recipeHtml = 'recipe';
      that.searchHelper({
        data: data,
        typeName: 'recipes',
        elemHtml: recipeHtml,
        elemsHtml: recipesHtml,
        searchName: 'and'
      });

      var productsHtml = '<ol id="products-list"></ol>';
      var productHtml = 'product';
      that.searchHelper({
        data: data,
        typeName: 'products',
        elemHtml: productHtml,
        elemsHtml: productsHtml,
        searchName: 'and'
      });

      var lifeStylesHtml = '<ol id="lifeStyles-list"></ol>';
      var lifeStyleHtml = 'lifeStyle';
      that.searchHelper({
        data: data,
        typeName: 'lifestyle',
        elemHtml: lifeStyleHtml,
        elemsHtml: lifeStylesHtml,
        searchName: 'and'
      });
    });
 
  },

  searchHelper: function(args) {
    var data = args.data;
    var typeName = args.typeName;
    var elemHtml = args.elemHtml;
    var elemsHtml = args.elemsHtml;
    var searchName = args.searchName;
    data = data[searchName][typeName];

    if(data.length > 0) {
      data = data.slice(0,3);
      $(data).each(function(i, ele){
        elemHtml += `<li><a href="/${typeName}/${ele.id}">${ele.name}</a></li>`;
      });

      $('#search-' + searchName).append(elemsHtml);
      $(`#${typeName}-list`).html(elemHtml);
    }
  },

  render:function(){
    var message = this.state.message;
    return (
      <div className="input-group">
        <input type="text" className="form-control" value={message} onChange={this.handleChange} onKeyUp={this.handleKeyUp} placeholder="Search for..." />
        <span className="input-group-btn">
          <button className="btn btn-default" type="button">Go!</button>
        </span>
      </div>
    )
  }
});

module.exports = searchBox;