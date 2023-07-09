3 .Create a Node.js file that Insert Multiple Records in "student" table, and 
display the result object on console. 
const mysql = require('mysql'); 
// Create a connection to the MySQL database 
const connection = mysql.createConnection({ 
host: 'localhost', 
user: 'your_username', 
password: 'your_password', 
database: 'your_database' 
}); 
// Connect to the database 
connection.connect((err) => { 
if (err) { 
console.error('Error connecting to the database: ' + err.stack); 
return; 
} 
console.log('Connected to the database as ID: ' + connection.threadId); 
}); 
// Define the array of student records to be inserted 
const students = [ 
{ name: 'John Doe', age: 20, grade: 'A' }, 
{ name: 'Jane Smith', age: 19, grade: 'B' }, 
{ name: 'David Johnson', age: 21, grade: 'A+' } 
// Add more student records as needed 
]; 
// Insert multiple records into the "student" table 
connection.query('INSERT INTO student (name, age, grade) VALUES ?', [students.map(student => 
[student.name, student.age, student.grade])], (err, result) => { 
if (err) { 
console.error('Error inserting records: ' + err.stack); 
return; 
} 
console.log('Records inserted successfully!'); 
console.log('Affected rows: ' + result.affectedRows); 
console.log('Inserted rows: ' + result.insertedRows); 
}); 
// Close the database connection 
connection.end((err) => { 
if (err) { 
console.error('Error closing the database connection: ' + err.stack); 
return; 
} 
console.log('Database connection closed.'); 
}); 