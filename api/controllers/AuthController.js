/**
 * AuthController
 *
 * @description :: Server-side logic for managing auths
 * @help        :: See http://sailsjs.org/#!/documentation/concepts/Controllers
 */

var passport = require('passport');

module.exports = {

  _config: {
    actions: false,
    shortcuts: false,
    rest: false
  },

  login: function(req, res) {
    passport.authenticate('local', function(err, user, info) {
      if((err) || (!user)) {
        return res.send({
          message: info.message,
          user: user
        });
      }
      req.login(user, function(err) {
        if(err) res.send(err);
        return res.send({
          message: info.message,
          user: user
        });
      });
    })(req, res);
  },

  logout: function(req, res) {
    req.logout();
    res.redirect('/');
  },

  signup: function(req, res) {
    User.create({email: req.body.email, password:req.body.password}).exec(function createCB(err, data) {
      console.log(err, data);
      return res.redirect('/login');
    })
  }

};

