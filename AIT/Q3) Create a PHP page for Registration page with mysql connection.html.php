Q3) Create a PHP page for RegistraƟon page with MySQL connecƟon.
 RegistraƟonForm2.html:
<!DOCTYPE html> 
<html> 
 <head> 
 <Ɵtle>RegistraƟon Form</Ɵtle>
 </head> 
 <body> 
 <h2>RegistraƟon Form</h2>
 <form acƟon="RegistraƟonForm2.php" method="get">
 Enter your id: <input type="text" name="id"> <br><br> 
 Enter your name: <input type="text" name="name"> <br><br> 
 Enter your mobile number: <input type="text" name="mobno"> <br><br> 
 Enter your age: <input type="text" name="age"> <br><br> 
 Select your gender: 
 <input type="radio" name="gender" value="male">Male 
 <input type="radio" name="gender" value="female">Female 
 <input type="radio" name="gender" value="other">Other 
 <br><br> 
 Enter your email id: <input type="text" name="email"> <br><br> 
 Enter your username: <input type="text" name="username"> <br><br> 
 Enter your password: <input type="password" name="password"> <br><br> 
 <input type="submit" value="Submit"> 
 <input type="submit" value="Reset"> 
 </form> 
 </body> 
</html> 
 RegistraƟonForm2.php:
<?php 
 $id=$_GET['id']; 
 $name=$_GET['name']; 
 $mobno=$_GET['mobno']; 
 $age=$_GET['age']; 
 $gender=$_GET['gender']; 
 $email=$_GET['email']; 
 $username=$_GET['username']; 
 $password=$_GET['password']; 
 $servername="localhost"; 
 $dbusername="root"; 
 $dbpassword=""; 
 $dbname="testschema"; 
 $conn=mysqli_connect($servername,$dbusername,$dbpassword,$dbname); 
 if(!$conn) 
 die("ConnecƟon failed.".$conn->connect_error); 
 //print_r($conn); 
 $query="insert into user values 
('$id','$name','$mobno','$age','$gender','$email','$username','$password')"; 
 if(mysqli_query($conn,$query)) 
 echo "Record inserted successfully."; 
 else 
 echo "Error.".msqli_error(); 
 $conn->close(); 
?> 