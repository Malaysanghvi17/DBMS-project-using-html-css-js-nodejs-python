const express = require('express');
const mysql = require('mysql');

const app = express();
const port = 7890;

// Create a connection to the MySQL database
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'dbms_project',
});

// Connect to the MySQL database
connection.connect((err) => {
    if (err) {
        console.error('Error connecting to the database: ', err.stack);
        return;
    }

    console.log('Connected to the database.');
});

// Set up the body parser middleware
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

// Serve the static files in the public directory
app.use(express.static('public'));
// Route for submitting the form data
app.post('/submit-form', (req, res) => {
    const name = req.body.name;
    const roll = req.body.roll;
    const email = req.body.email;
    const contact = req.body.contact;
    const address = req.body.address;
    const birthdate = req.body.birthdate;
    const gender = req.body.gender;
    const course = req.body.course;
    const courseid = req.body.courseid;
    const stream = req.body.stream;
    const semester = req.body.semester;
    const cgpa = req.body.cgpa;
    const hobby = req.body.hobby;
    const about = req.body.about;

    console.log(name, roll, email, contact, address, birthdate, gender, course, courseid, stream, semester, cgpa, hobby, about);

    // Insert the data into the MySQL table
    const sql1 = `INSERT INTO student_info (name, roll, email, contact, address, birthdate, gender) VALUES (?, ?, ?, ?, ?, ?, ?)`;
    connection.query(sql1, [name, roll, email, contact, address, birthdate, gender], (err, result) => {
        if (err) {
            console.error('Error inserting data: ', err.stack);
            return res.status(500).send('Error inserting data into student_info database');
        }

        console.log('Data inserted successfully in student_info.');

        // Insert the data into the course table
        const sql2 = `INSERT INTO course (course, courseid, stream) VALUES (?, ?, ?)`;
        connection.query(sql2, [course, courseid, stream], (err, result) => {
            if (err) {
                console.error('Error inserting data: ', err.stack);
                return res.status(500).send('Error inserting data into course database');
            }

            console.log('Data inserted successfully in course.');


            // Insert the data into the student_course table
            const sql3 = `INSERT INTO student_course (roll,courseid, semester, cgpa) VALUES (?, ?, ?, ?)`;
            connection.query(sql3, [roll, courseid, semester, cgpa], (err, result) => {
                if (err) {
                    console.error('Error inserting data: ', err.stack);
                    return res.status(500).send('Error inserting data into student_course database');
                }

                console.log('Data inserted successfully in student_course.');

                // Insert the data into the student_hobbies_about table
                const sql4 = `INSERT INTO student_hobbies_about (roll,hobby,about) VALUES (?, ?, ?)`;
                connection.query(sql4, [roll, hobby, about], (err, result) => {
                    if (err) {
                        console.error('Error inserting data: ', err.stack);
                        return res.status(500).send('Error inserting data into student_hobbies database');
                    }
                    console.log('Data inserted successfully in student_hobbies and about.');

                // Insert the data into the student_hobbies table
                // const sql4 = `INSERT INTO student_hobbies (roll,hobby) VALUES (?, ?)`;
                // connection.query(sql4, [roll, hobby], (err, result) => {
                //     if (err) {
                //         console.error('Error inserting data: ', err.stack);
                //         return res.status(500).send('Error inserting data into student_hobbies database');
                //     }

                //     console.log('Data inserted successfully in student_hobbies.');


                //     // Insert the data into the student_about table
                //     const sql5 = `INSERT INTO student_about (roll, about) VALUES (?, ?)`;
                //     connection.query(sql5, [roll, about], (err, result) => {
                //         if (err) {
                //             console.error('Error inserting data: ', err.stack);
                //             return res.status(500).send('Error inserting data into student_about database');
                //         }

                //         console.log('Data inserted successfully in student_about.');
                //     });

                    const sql0 = `INSERT INTO form_data (name, roll, email, contact, address, birthdate, gender, course, courseid, stream, semester, cgpa, hobby, about) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? ,? ,?, ?)`;
                    connection.query(sql0, [name, roll, email, contact, address, birthdate, gender, course, courseid, stream, semester, cgpa, hobby, about], (err, result) => {
                        if (err) {
                            console.error('Error inserting data: ', err.stack);
                            return res.status(500).send('Error inserting data into form_data database');
                        }

                        console.log('Data inserted successfully in form_data.');
                        return res.send('Form submitted successfully!');
                    });
                });
            });
        });
    });
});


app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
// Close the database connection when the Node process ends
process.on('exit', () => {
    connection.end();
    console.log('Database connection closed.');
});