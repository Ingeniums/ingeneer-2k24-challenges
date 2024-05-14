const mysql = require('mysql2');

const initDb = () => {
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

        const createJokesTableQuery = `
            CREATE TABLE IF NOT EXISTS jokes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                joke TEXT NOT NULL,
                category VARCHAR(255)
            )
        `;
        db.query(createJokesTableQuery, (err) => {
            if (err) {
                console.error('Error creating jokes table:', err.message);
                return;
            }
            console.log('Jokes table created or already exists');

            const initialJokes = [
                ["Why don't scientists trust atoms? Because they make up everything!", "Science"],
                ["Parallel lines have so much in common. It's a shame they'll never meet.", "Math"],
                ["I'm reading a book on the history of glue. I just can't seem to put it down!", "Puns"]
            ];
            const insertJokesQuery = 'INSERT INTO jokes (joke, category) VALUES ?';
            db.query(insertJokesQuery, [initialJokes], (err) => { });
        });

        const createQuotesTableQuery = `
            CREATE TABLE IF NOT EXISTS quotes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                quote TEXT NOT NULL,
                author VARCHAR(255)
            )
        `;
        db.query(createQuotesTableQuery, (err) => {
            if (err) {
                console.error('Error creating quotes table:', err.message);
                return;
            }
            console.log('Quotes table created or already exists');

            const initialQuotes = [
                ["The greatest glory in living lies not in never falling, but in rising every time we fall.", "Nelson Mandela"],
                ["The way to get started is to quit talking and begin doing.", "Walt Disney"],
                ["If life were predictable it would cease to be life, and be without flavor.", "Eleanor Roosevelt"]
            ];
            const insertQuotesQuery = 'INSERT INTO quotes (quote, author) VALUES ?';
            db.query(insertQuotesQuery, [initialQuotes], (err) => { });
        });
    });
};

module.exports = initDb;
