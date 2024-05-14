require('dotenv').config()
const express = require('express');
const bodyParser = require('body-parser');
const session = require('express-session');
const sqlite3 = require('sqlite3').verbose();
const initDb = require('./initDb');

const app = express();


const db = new sqlite3.Database('database.db');


app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');


app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(session({
    secret: 'wrwerj3223e29u9uofsjflwjlw555fff',
    resave: true,
    saveUninitialized: true
}));

app.set('view engine', 'ejs');

const port = 3000

const FLAG = process.env.FLAG || "ingeneer{fake_flag}"


app.get('/', (req, res) => {
    if (req.session && req.session.isLoggedIn) {
        return res.redirect('/secret')
    } else {
        return res.render('home');
    }
});

app.get('/secret', (req, res) => {
    if (!req.session || !req.session.isLoggedIn) {
        res.redirect('/')
    } else {
        const isAdmin = req.session.isAdmin
        const flag = isAdmin ? FLAG : "Only rik0s can see the flag"
        res.render('secret', { flag });
    }

});

app.get('/register', (req, res) => {
    if (req.session && req.session.isLoggedIn) {
        res.redirect('/secret')
    } else {
        res.render('register', { message: ""});
    }

});

app.get('/logout', (req, res) => {
    if (req.session && req.session.isLoggedIn) {
        req.session.destroy((err) => {
            if (err) {
                console.error('Error destroying session:', err.message);
                return res.status(500).send('Error destroying session');
            }
            res.redirect('/login');
        });
    } else {
        res.redirect('/login');
    }
});
app.post('/register', (req, res) => {
    const { username, password } = req.body;
    
    const checkUsernameQuery = `
        SELECT COUNT(*) as count
        FROM users
        WHERE username = ?
    `;
    
    db.get(checkUsernameQuery, [username], (err, row) => {
        if (err) {
            console.error('Error checking username:', err.message);
            return res.render('register', { message: 'Error registering user' });
        }

        if (row.count > 0) {
            return res.render('register', { message: 'Username already exists' });
        } else {
            const insertQuery = `
                INSERT INTO users (username, password, isAdmin)
                VALUES (?, ?, ?)
            `;
            db.run(insertQuery, [username, password, 0], function (err) {
                if (err) {
                    console.error('Error registering user:', err.message);
                    return res.render('register', { message: 'Error registering user' });
                }
                res.render('login', { message: "Registered successfully, now you can login" });
            });
        }
    });
});



app.get('/login', (req, res) => {
    if (req.session && req.session.isLoggedIn) {
        res.redirect('/secret')
    } else {
        res.render('./login', { message: ''})
    }

});

app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    console.log(username, password)
    try {
        const selectQuery = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
        console.log("qeruy" + selectQuery)
        db.get(selectQuery, [], (err, row) => {
            if (err) {
                console.log(err)
                return res.render('login', { message: 'Something went wrong'});
            }
            if (!row) {
                return res.render('login', { message: 'No user found' });
            }
            if (row) {
                console.log("row" + row.username)
                req.session.isLoggedIn = true;
                req.session.isAdmin = row.isAdmin;
                req.session.username = username;
                return res.redirect('/');
            }

        });

    } catch (err) {
        console.log(err)
        console.log("something wronge happend")
        res.render('./login', { message: "Authentication failed" });
    }
});



initDb()

app.listen(3000, () => {
    console.log(`Server is running at port ${port}`);
});