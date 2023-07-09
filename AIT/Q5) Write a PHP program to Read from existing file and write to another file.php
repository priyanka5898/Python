Q5) Write a PHP program to Read from exisƟng file and write to 
another file.
 CopyFileContents.php: 
<?php 
 $sourceFile="file1.txt"; 
 $desƟnaƟonFile="file2.txt";
 if(!copy($sourceFile,$desƟnaƟonFile))
 echo "File contents could not be copied."; 
 else 
 echo "File contents were copied successfully."; 
?>