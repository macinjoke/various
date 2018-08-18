module.exports = {
  entry: {
    main: ['babel-polyfill', './src/index.js'],
  },
  module: {
    rules: [
      {
        test: /.js?$/,
        use: 'babel-loader',
        exclude: /node_modules/,
      },
    ],
  },
  devServer: {
    contentBase: 'dist',
  }
}
