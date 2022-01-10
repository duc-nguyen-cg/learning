var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: '',
        pass: ''
    }
});

var mailOptions = {
    from: '',
    to: '',
    subject: 'Sending email using Node.js',
    text: 'Gunslinger Girl'
};

transporter.sendMail(mailOptions, function(err, info){
    if (err) {
        console.log(err);
    } else {
        console.log('Email sent: '+ info.response);
    }
});

