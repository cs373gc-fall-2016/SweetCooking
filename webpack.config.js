var webpack = require('webpack');
module.exports = {
  entry: [
    "./client/app.js"
  ],
  output: {
    path: './app/static/javascripts',
    filename: "bundle.js"
  },
  module: {
    loaders: [
      {
        test: /\.js?$/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'react']
        },
        exclude: /node_modules/
      },
      {test: /\.css$/, loader: 'style-loader!css-loader'}
    ]
  },
  plugins: [
  ]
};
