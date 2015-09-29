/**
 * Created by prism on 9/29/15.
 */
Router.configure({
    layoutTemplate: 'layout',
    loadingTemplate: 'loading',
    notFoundTemplate: 'notFound'
});

Router.route('/contact', function (){
    //name: 'contact',
    this.render('contact');
});