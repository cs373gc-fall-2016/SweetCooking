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
    $.ajax({
      url: `/api/search/all?term=${searchPhrase}`,
      beforeSend: function() {
      },
    }).done(function(data) {
      that.resetUI();
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
 
  },

  searchDriver: function(args) {
    var that = this;

    var data = args.data;
    var searchType = args.searchType;
    var searchP = args.searchP;


    var ingredientsHtml = '<ol class="ingredients-list"></ol>';
    var ingredientHtml = 'Ingredient';

    that.searchHelper({
      data: data,
      typeName: 'ingredients',
      searchType: searchType,
      searchP: searchP,
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
  },

  searchHelper: function(args) {
    var that = this;
    var data = args.data;
    var searchP = args.searchP;
    var typeName = args.typeName;
    var searchType = args.searchType;
    var elemHtml = args.elemHtml;
    var elemsHtml = args.elemsHtml;

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
        that.searchDataProcess({
          data: temp,
          typeName: typeName,
          searchP: searchP,
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
    var searchP = args.searchP;
    
    if(data.length > 0) {
      if(searchType == 'or') {
        elemHtml = key;
      }
      data = data.slice(0,10);

      for(var i =0; i<data.length; i++){
        data[i]['searchP'] = searchP;
      }

      
      $(data).each(function(i, ele){
        ele.name = ele.name.toLowerCase();
        ele.searchP = ele.searchP.toLowerCase();
        var y = ele.searchP.split(" ");
        for(var i = 0; i < y.length; i++) {
          ele.name = ele.name.split(y[i]).join('<span style="background-color: yellow;">'+y[i]+'</span>')
          }
          if(typeName == "products" ) {
            typeName = 'foodproducts';
            elemHtml += `<li><a href="/${typeName}/${ele.id}">${ele.name}</a></li>`;
            typeName = 'products';
          } else {
            elemHtml += `<li><a href="/${typeName}/${ele.id}">${ele.name}</a></li>`; 
          }
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

  highlightSearchPhrase: function(elementName, searchPhrase) {

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