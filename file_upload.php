<?php
   $target_dir = "/home/harish/Burnout_Predictor/Burnout_Prediction_Python/upload_files/";
   $target_file = $target_dir.$_FILES["fileToUpload"]["name"];
   $file_name = $_FILES["fileToUpload"]["name"];
   $flag = 0;
   if(move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)){
       #echo "File has been uploaded";
       $flag = 1; 
   }
   else{
       echo "File not yet uploaded";
       echo move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file);
   }
   if($flag == 1){
     $pyex = shell_exec("/home/harish/pyopcv/bin/python3 /home/harish/Burnout_Predictor/Burnout_Prediction_Python/mental_health.py '$file_name'");
     //echo $pyex;
     //include 'result.html';
     header("Location: result.html");
     exit();
   }



?>
