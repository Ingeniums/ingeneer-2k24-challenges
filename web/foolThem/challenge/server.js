require('dotenv').config();
const express = require('express');
const app = express();
const path = require('path');
const crypto = require('crypto');
const geoip = require('geoip-lite');

app.use(express.static(path.join(__dirname, 'public')));

app.use((req, res, next) => {
    const allowedHeader = req.headers.allowed;
    if (allowedHeader || req.path === '/') {
        if(req.path === '/flag-page'){
        const clientIP = req.headers['x-forwarded-for'] || req.ip;
        var geo = geoip.lookup(clientIP);
          if (geo && geo.country === 'US' && geo.region === "VA" ) {
            next();
        } else {
            res.status(403).send( (`<html>
            <head>
                <title>Access Forbidden</title>
            </head>
            <body>
            <div style="display: flex;align-items: center;justify-content: center;flex-direction: column;" >
                <h1>Access Forbidden</h1>
                <p>I'm not sure that you are from the saviors to let you in.the people from our region does not have id value like yours .</p>
                <img src="Saviors.webp" style="height: 400px;width: 400px;"  alt="Saviors logo">
                </div>
            </body>
        </html>
    `));
        }
        }else{
        next();
        }
    } else if(req.path === '/sitemap.xml' ) {
      console.log('ss')
               res.status(401).header('allowed', false).send((`<html>
            <head>
                <title>Not Allowed</title>
            </head>
            <body>
            <div style="display: flex;align-items: center;justify-content: center;flex-direction: column;" >
                <h1>You are not allowed</h1>
                <img src="not_allowed.gif" style="height: 400px;width: 400px;"  alt="Saviors logo">
                </div>
            </body>
        </html>
    `));
    } else{
      console.log('3')
             res.redirect('/'); 
    }
});

const sitemapContent = `
<sitemap>
    <url>${process.env.URL}/flag-page</url>
</sitemap>
`;

app.get('/sitemap.xml', (req, res) => {
    res.type('application/xml');
    res.send(sitemapContent);
});

app.get('/flag-page', (req, res) => {

const flag = 'ingeneer{91b_Chibs1}';
const algorithm = 'aes-256-cbc';
const key = crypto.randomBytes(32);
console.log('ss',key)
const iv = crypto.randomBytes(16);

const cipher = crypto.createCipheriv(algorithm, key, iv);

let encrypted = cipher.update(flag, 'utf8', 'hex');
encrypted += cipher.final('hex');

const decipher = crypto.createDecipheriv(algorithm, key, iv);

let decrypted = decipher.update(encrypted, 'hex', 'utf8');
decrypted += decipher.final('utf8');

console.log('Original text: ', flag);
console.log('key: ', key.toString('hex'));
console.log('Encrypted text: ', encrypted);
console.log('Decrypted text: ', decrypted);
  
    const storeKeyScript = `
        <script>
   localStorage.setItem('Key','${key.toString('hex')}');
        </script>
    `;

    const htmlResponse = `
    <html>



    
            <head>
                <title>
                Access 
                Forbidden
                </title>
            </head>

            
            <body>
             <div 
                style=
                "display: 
                flex;
                align-items:
                 center;
                 justify-content:
                  center;
                  flex-direction:
                   column;
                   ">
                    <p>
                    The flag:
                     ${encrypted}
                     </p>
                    <p>
                    The message 
                    is encrypted 
                    because
                     we want it
                      to be secure.
                       If you are
                        who you say you are,
                         you should know
                          how to decrypt it.
                    </p>
              </div>
            </body>
               ${storeKeyScript}
    </html>
    `;

    res.header({'Hash-algo': 'AES-256-CBC', 'iv': iv.toString('hex')}).send(htmlResponse);

});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const PORT = 3000
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
