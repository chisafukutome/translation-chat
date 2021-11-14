requirejs([])

let mysql = require('mysql');

function sign_up(form) {
    let connection = mysql.createConnection({
        host: '34.138.14.68',
        user: 'root',
        password: 'Pass2546',
        database: 'speakme_data'
    });

    let un = form.getElementById("input-username").value;
    let pw = form.getElementById("input-password").value;
    let lang = form.getElementById("dropdown").value;

    try {
        connection.connect(function (err) {
            if (err) throw err;
            console.log("Connection established");
        });

        let sql = `INSERT INTO users (username, password, language)
                   VALUES (:un, :pw, :lang)`;

        connection.end();
        return 1;
    } catch (e) {
        console.log(e);
    }
    return undefined;
}

function log_in(form) {
    let connection = mysql.createConnection({
        host: '34.138.14.68',
        user: 'root',
        password: 'Pass2546',
        database: 'speakme_data'
    });

    let un = form.getElementById("input-username").value
    let pw = form.getElementById("input-password").value

    try {
        connection.connect(function (err) {
            if (err) throw err;
            console.log("Connection established");
        });

        let sql = `SELECT (username, password)
                   FROM users
                   WHERE username = ?
                     AND password = ?`;
        connnection.query(sql, [un, pw], (error, result) => {
            if (error) {
                return console.error(error.message);
            }
            console.log(result);
        });
        connection.end();
        return 1;
    } catch (e) {
        console.log(e);
    }
    return undefined;
}
