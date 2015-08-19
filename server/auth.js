/**
 * Created by prism on 8/16/15.
 */

var database = new MongoInternals.RemoteCollectionDriver("mongodb://127.0.0.1:3001/hiren_pirate");
User = new Mongo.Collection("user", { _driver: database });
