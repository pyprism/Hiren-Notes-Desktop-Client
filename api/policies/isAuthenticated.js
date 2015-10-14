/**
 * Created by prism on 10/14/15.
 */
module.exports = function(req, res, next) {
  if (req.isAuthenticated()) {
    return next();
  }
  else{
    return res.redirect('/login');
  }
};
