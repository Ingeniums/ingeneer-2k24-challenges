require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');
const initDb = require('./initDb');

const app = express();

const db = mysql.createConnection({
    host: process.env.DB_HOST || 'mysql',
    user: process.env.DB_USER || 'notroot',
    password: process.env.DB_PASSWORD || 'pass',
    port: process.env.DB_PORT || '3306',
    database: process.env.DB_NAME || 'db',
});

db.connect((err) => {
    if (err) {
        console.error('Error connecting to MySQL:', err.message);
        return;
    }

    console.log('Connected to MySQL database');
    initDb();
    app.listen(port, () => {
        console.log(`Server is running at port ${port}`);
    });
});


app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


const port = 3000;


app.get('/', (req, res) => {
    res.render('home');
});

app.post('/content', (req, res) => {
    const { column, table } = req.body;

    const db = mysql.createConnection({
        host: process.env.DB_HOST || 'mysql',
        user: process.env.DB_USER || 'notroot',
        password: process.env.DB_PASSWORD || 'pass',
        port: process.env.DB_PORT || '3306',
        database: process.env.DB_NAME || 'db',
    });

    const query = `SELECT ?? FROM ??`;
    const values = [column, table];

    db.query(query, values, (err, results) => {
        if (err) {
            console.error('Error fetching content:', err.message);
            return res.status(500).send('Error fetching content');
        }
        const content = results.map(row => row[column]);
        console.log(content);
        res.render('content', { table, content });
    });

    db.end();
});





