<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
            // Retrieve form fields var_dump($_POST);

        $first_name =  (string) $_POST['first-name'];
        $last_name = (string) $_POST['last-name'];
        $message = (string) $_POST['text-field'];
        $email_subject = (string) $_POST["subject"];
    
        // Create a connection
        $conn = new mysqli('localhost', 'bill', '1771999bs', 'email_db');

        // Check the connection
        if ($conn->connect_error) {
            die("<script>alert(Connection failed)</script>");
        }
        else {
            $sql = "INSERT INTO person_info (first_name,last_name,subject,email_text) VALUES ('$first_name','$last_name', '$email_subject','$message')";
            $result = $conn->query($sql);

            $sql = "SELECT * FROM person_info";
            $result = $conn->query($sql);
            
            $conn->close();
            }
    }
?>