#!/usr/bin/node
const process = require('process');
const request = require('request');

request('https://swapi-api.hbtn.io/api/films' + process.argv[2], function (error, respones, body) {
  if (error) {
    console.log(error);
  } else {
     console.log(JSON.parse(body).title);
  }
});