// Importing module
var mysql = require('mysql');

var con = mysql.createConnection({
	host:"mysql",
	user:"root",
	password:"1234",
	database : "project_kub"
});

// Connecting to database
con.connect(function(err) {
  if (err) throw err;
  con.query("INSERT INTO table1 (time_stamp) VALUE (CURRENT_TIME())", function (err, result, fields) {
    if (err) throw err;
    console.log(result);
  });
  con.query("INSERT INTO table1 (time_stamp) VALUE (CURRENT_TIME())", function (err, result, fields) {
    if (err) throw err;
    console.log(result);
  });
  con.end();
});
