var fs = require('fs');

//  if the file already exists, append
fs.readFile('demofile1.html', function(err, data){
    fs.appendFile('mynewfile1.txt', data, function(err) {
        if (err) throw err;
        console.log('Saved!');
    });
});
