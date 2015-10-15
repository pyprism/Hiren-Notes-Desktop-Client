/**
 * PostController
 *
 * @description :: Server-side logic for managing posts
 * @help        :: See http://sailsjs.org/#!/documentation/concepts/Controllers
 */

module.exports = {

  index: function(req, res) {
    res.render('admin/dashboard', {'saved': false});
  },

  editor: function(req, res) {
    Post.create({title:req.body.title, content:req.body.content, category:req.body.category}).exec(function createPost(err, data) {
      if (err) {
        return res.json(err);
      }
      else {
        return res.view('admin/dashboard', {'saved':true, 'data': data.id});
      }
    });
  }
};

