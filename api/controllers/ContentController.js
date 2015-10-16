/**
 * ContentController
 *
 * @description :: Server-side logic for managing contents
 * @help        :: See http://sailsjs.org/#!/documentation/concepts/Controllers
 */

module.exports = {
  _config: {
    actions: false,
    shortcuts: false,
    rest: false
  },

  index: function(req, res) {
    res.render('index');
  },

  content: function(req, res) {
    //console.log(Post.find().where({category: req.param('category')}).paginate({page: req.param('page', 0), limit: 10}))
    Post.find().where({category: req.param('category')}).paginate({page: req.param('page'), limit: 10}).exec(function Hiren(err, data) {
        console.log(data);
    });
    res.end("S");
  }
};

