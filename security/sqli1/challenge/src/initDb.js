const sqlite3 = require('sqlite3').verbose();

const initDb = () => {
    const db = new sqlite3.Database('database.db');

    db.serialize(() => {
        db.run(`CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            isAdmin INTEGER DEFAULT 0
        )`, (err) => {
            if (err) {
                console.error('Error creating users table:', err.message);
            } else {
                console.log('Users table created or already exists');
            }
        });

        db.get('SELECT COUNT(*) AS count FROM users', (err, row) => {
            if (err) {
                console.error('Error checking user count:', err.message);
            } else {
                const count = row.count;
                if (count < 2) {
                    // Perform both inserts if there are less than 2 users
                    db.run(`INSERT INTO users (username, password, isAdmin) VALUES (?, ?, ?)`, ['notrik0s', 'NPncUIxtk7IWppS', 0], (err) => {
                        if (err) {
                            console.error('Error inserting default user:', err.message);
                        } else {
                            console.log('Default user inserted');
                        }
                    });

                    db.run(`INSERT INTO users (username, password, isAdmin) VALUES (?, ?, ?)`, ['rik0s', 'NPncUIxtk7IWppSNPncUIxtk7IWppS', 1], (err) => {
                        if (err) {
                            console.error('Error inserting default user:', err.message);
                        } else {
                            console.log('Default user inserted');
                        }
                    });
                }
            }

            db.close((err) => {
                if (err) {
                    console.error('Error closing database connection:', err.message);
                } else {
                    console.log('Database connection closed');
                }
            });
        });
    });
};

module.exports = initDb;
