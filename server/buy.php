<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Hello There</title>
	<style> 
        body { 
            font-family: 'Arial', sans-serif; /* Шрифт для всего тела страницы */ 
            background: linear-gradient(to right, #e0f7fa, #80deea); /* Градиентный фон */ 
            margin: 0; 
            padding: 20px; 
            text-align: center; /* Выравнивание текста по центру */ 
        } 

        h2 { 
            color: #004d40; /* Цвет заголовка */ 
            margin-top: 20px; 
        } 

        .btn { 
            display: inline-block; /* Строчно-блочный элемент */ 
            background: #00796b; /* Темно-зеленый цвет фона */ 
            color: #fff; /* Белый цвет текста */ 
            padding: 1rem 1.5rem; /* Поля вокруг текста */ 
            text-decoration: none; /* Убираем подчеркивание */ 
            border-radius: 5px; /* Скругляем уголки */ 
            margin-top: 20px; /* Отступ сверху */ 
            transition: background 0.3s, transform 0.2s; /* Плавный переход цвета и эффекта наведения */ 
        } 

        .btn:hover { 
            background: #004d40; /* Цвет кнопки при наведении */ 
            transform: scale(1.05); /* Увеличение кнопки при наведении */ 
        } 

        .error { 
            color: red; /* Цвет для сообщений об ошибках */ 
            margin-top: 20px; 
        } 

        .success { 
            color: green; /* Цвет для успешных сообщений */ 
            margin-top: 20px; 
        }
    </style> 
    </head>
    <body>
        <?php
            $buy_code = 0;
            $username = "Not found";

            if(isset($_GET["buy_code"])){
                $buy_code = $_GET["buy_code"];
            }

            if(isset($_GET["username"])){
                $username = $_GET["username"];
            }

	    $IP_V4 = "http://192.168.0.161";
            $serv = "localhost"; //Нужно будет поменять на сервер Георгия, либо оставить, если запускаем с его ноута
            $root = "root"; 
            $password = "";//пароль Георгия
            $database = "DB_SEEKSHELP";//datafuckinbase

            $conn = new mysqli($serv, $root, $password, $database); //соединение с базой данных

            $sql = "SELECT points FROM site WHERE username = '$username'"; //Выводим рейтинг нашего чела
            $points_before = 0;
            if($result = $conn->query($sql)){
                $rowsCount = $result->num_rows; //количество полученых из базы данных строк

                foreach($result as $row){
                    $points_before = $row["points"]; //zapisivaem balli
                }

                $result->free(); //освобождаем память
            }
            
            switch($buy_code)
            {
            case 1: 
                $points_after = $points_before - 1000;
                break;
            case 2: 
                $points_after = $points_before - 700;
                break;
            case 3: 
                $points_after = $points_before - 100;
                break;
            case 4: 
                $points_after = $points_before - 400;
                break;
            case 5:
                $points_after = $points_before - 120;
                break;
            }

            $sql1 = "UPDATE site SET points = '$points_after' WHERE username = '$username'";
            if($result = $conn->query($sql1)){
                echo "<h2>Обмен прошёл успешно ,поздравляем))</h2>";
		echo "<a href='$IP_V4/bot_project/main.php?username=$username' class='btn'>Окей</a>";
            } else{
                echo "Ошибка: " . $conn->error;
            }

        ?>
        
    </body>
</html>