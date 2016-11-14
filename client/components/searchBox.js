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
      that.resetUI();
    }
    // console.log("testing: " + this.state.message);

  },

  handleKeyUp: function() {
    var that = this;
    if(this.state.message === ''){
      that.resetUI();
    }
    if($('.fa-spinner').length < 1) {
      $('#spinner').html('<i class="fa fa-spinner fa-pulse fa-4x fa-fw"></i>');
      $('#spinner').css("padding-top", "20px");
    }
    // console.log("this is outside: " + this.state.message);
    // run only once per search
    clearTimeout(window.timer);
    window.timer = setTimeout(function() {
      if(that.state.message !== '') {
        that.doSearch(that.state.message);
      }
      else {
        that.resetUI();
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
      that.resetUI();
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
 
  },

  searchDriver: function(args) {
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
  },

  searchHelper: function(args) {
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
  },

  searchDataProcess: function(args) {
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
  },

  resetUI: function() {
    $('#spinner').html('');
    $('#spinner').removeAttr('style');
    $('#search-and').html('');
    $('#search-or').html('');
  },

  render: function(){
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