"use strict"
const express = require('express');
const app = express();
const key = require('./api_key');
const twitter_client = require('./twiter');
const winston = require('winston');
const method_override = require('method-override');
const body_parser = require('body-parser');
const passport = require('passport');
const TwitterStrategy = require('passport-twitter').Strategy;
const session = require('express-session');
const request = require("request");
let logger = new winston.Logger({
	transports:[
		new winston.transports.File({
			level:'info',
			filename:'logs.log',
			handleException:true,
			json:true,
			maxsize:542880,
			maxFiles:5,
			colorize:true
		}),
		new winston.transports.Console({
			level:'debug',
			handleException:true,
			colorize:true
		})
	],
	exitOnError:false
});
logger.stream = {
	write: (message,encoding)=>{
		logger.info(message);
	}
};
app.use(require('morgan')("combined",{"stream":logger.stream}));
app.use(session({
	secret:'Don',
	resave:true,
	saveUninitialized:true
}));

app.use(body_parser.urlencoded({'extended':true}));
app.use(body_parser.json());
app.use(body_parser.json({type:'application/vdn.api+json'}));
app.use(method_override('X-HTTP-Method-Override'));
app.use( passport.initialize());
app.use( passport.session());
passport.use(new TwitterStrategy({
    consumerKey: key.TWITTER_CONSUMER_KEY,
    consumerSecret: key.TWITTER_CONSUMER_SECRET,
    callbackURL: "http://127.0.0.1:3000/auth/twitter/callback"
  },
  function(token, tokenSecret, profile, cb) {
  	console.log(twitter_client.get_user_list(profile.id));
  }
));
console.log(passport.authenticate);
app.get("/",(req,res,next)=>{
  res.send("Hello World");
  res.end("Request to root was made");
})
app.get('/auth/twitter',
  passport.authenticate('twitter'));

app.get('/auth/twitter/callback', 
  passport.authenticate('twitter', { failureRedirect: '/login' }),
  function(req, res) {
    // Successful authentication, redirect home.
    res.redirect('/');
});
console.log("Listening on port 3000");
app.listen(3000);
