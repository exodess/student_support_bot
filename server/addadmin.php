<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Главное окно</title>
<style> 
        body { 
            font-family: 'Arial', sans-serif; 
            background-color: #e3f2fd; /* Светло-голубой фон */ 
            margin: 0; 
            padding: 20px; 
            text-align: center; 
        } 

        h2 { 
            color: #4caf50; /* Цвет заголовка успешного добавления/изменения */ 
            margin-top: 20px; 
        } 

        .container { 
            background-color: #fff; /* Белый фон для контейнера */ 
            border-radius: 10px; /* Закругленные углы */ 
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Тень для блока */ 
            padding: 20px; 
            margin: 20px auto; 
            max-width: 600px; /* Максимальная ширина контейнера */ 
        } 

        .button { 
            background-color: #2196F3; /* Синий цвет кнопки */ 
            color: white; 
            padding: 10px 20px; 
            border: none; 
            border-radius: 5px; 
            cursor: pointer; 
            text-align: center; 
            text-decoration: none; 
            display: inline-block; 
            margin-top: 20px; 
            transition: background 0.3s; 
        } 

        .button:hover { 
            background-color: #1976D2; /* Более тёмный синий при наведении */ 
        } 
    </style> 
  </head>
  <body>
    <?php
        $new_admin = "Not found";
	$rat_change = "Not found";
	$new_rat = 0;
        if(isset($_GET["new_admin"])){
            $new_admin = $_GET["new_admin"];

            $IP_V4 = "http://192.168.0.124";
            $serv = "localhost"; //Нужно будет поменять на сервер Георгия, либо оставить, если запускаем с его ноута
            $root = "root"; 
            $password = "";//пароль Георгия
            $database = "DB_SEEKSHELP";//datafuckinbase

            $conn = new mysqli($serv, $root, $password, $database); //соединение с базой данных

            if($conn->connect_error){ //отслеживаем ошибку
                die("Ошибка: " . $conn->connect_error);
            }

            $sql = "INSERT INTO `admins` (`username`) VALUES ('$new_admin')";
            $conn->query($sql);

            echo "<h2>Админ успешно добавлен</h2>";
            $conn->close();
        }
	
	if(isset($_GET["rat_change"]) && isset($_GET["new_rat"])){
	    $rat_change = $_GET["rat_change"];
	    $new_rat = $_GET["new_rat"];

	    $IP_V4 = "http://192.168.0.124";
            $serv = "localhost"; //Нужно будет поменять на сервер Георгия, либо оставить, если запускаем с его ноута
            $root = "root"; 
            $password = "";//пароль Георгия
            $database = "DB_SEEKSHELP";//datafuckinbase

            $conn = new mysqli($serv, $root, $password, $database); //соединение с базой данных

            if($conn->connect_error){ //отслеживаем ошибку
                die("Ошибка: " . $conn->connect_error);
            }

            $sql = "UPDATE offers_help SET rating = '$new_rat' WHERE username = '$rat_change'";
            $conn->query($sql);

            echo "<h2>Рейтинг успешно изменён</h2>";
            $conn->close();

	    
        }
    ?>
  </body>
