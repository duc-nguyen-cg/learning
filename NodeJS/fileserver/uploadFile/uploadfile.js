var formidable = require('formidable');
var fs = require('fs');
var http = require('http');

http.createServer(function (req, res) {
    if (req.url == '/fileupload') {
      var form = new formidable.IncomingForm();
      form.parse(req, function (err, fields, files) {
        var oldpath = files.filetoupload.filepath;
        var newpath = 'C:/Users/nnduc1/Downloads/' + files.filetoupload.originalFilename;
        fs.rename(oldpath, newpath, function (err) {
          if (err) throw err;
          res.write('File uploaded and moved!');
          res.end();
        });
   });
    } else {
        fs.readFile('fileuploadform.html', function(err, fileuploadform){
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(fileuploadform);
            res.end();
        });      
    }
  }).listen(8080);

