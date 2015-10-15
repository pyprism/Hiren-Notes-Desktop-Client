/**
* Post.js
*
* @description :: TODO: You might write a short summary of how this model works and what it represents here.
* @docs        :: http://sailsjs.org/#!documentation/models
*/

module.exports = {

  attributes: {
    title: {
      type: 'string',
      required: true,
      unique: true
    },

    content: {
      type: 'text',
      required: true
    },

    slug: function() {
      return this.title.toString().toLowerCase().replace(/\s+/g, '-')
        .replace(/[^\w\-]+/g, '').replace(/\-\-+/g, '-')
        .replace(/^-+/, '').replace(/-+$/, '');
    },

    category: {
      type: 'string',
      enum: ['Movie', 'Album', 'Gents', 'Ladies', 'Technology']

    }

  }

/*  beforeCreate: function (post, cb) {
    post.slug = post.slug.toString().toLowerCase().replace(/\s+/g, '-')
      .replace(/[^\w\-]+/g, '').replace(/\-\-+/g, '-')
      .replace(/^-+/, '').replace(/-+$/, '');
    cb();
  }*/
};

