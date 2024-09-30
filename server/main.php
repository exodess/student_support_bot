<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"> 
        <title>Главное окно</title>
	<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        <style> 
        body { 
            font-family: 'Roboto', sans-serif; /* Используем шрифт Roboto */
            background: linear-gradient(to right, #e0f7fa, #80deea); /* Нежный градиентный фон */ 
            margin: 0; 
            padding: 20px; 
            text-align: center; /* Выравнивание текста по центру */ 
        } 

        h2, h3 { 
            color: #006064; /* Темно-синий цвет заголовков */ 
            margin: 20px 0; /* Отступы сверху и снизу заголовков */ 
            font-weight: 700; /* Жирный шрифт для заголовков */ 
        } 

        table { 
            width: 80%; /* Ширина таблицы */ 
            margin: 20px auto; /* Центрирование таблицы */ 
            border-collapse: collapse; 
            background-color: #ffffff; /* Белый цвет фона таблицы */ 
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Тень таблицы */ 
            border-radius: 10px; /* Закругленные углы таблицы */ 
            overflow: hidden; /* Обрезка содержимого для закругленных углов */ 
        } 

        th, td { 
            padding: 12px; 
            text-align: center; /* Выравнивание текста в ячейках по центру */ 
            border-bottom: 1px solid #e0e0e0; 
        } 

        th { 
            background-color: #0097a7; /* Цвет фона заголовков */ 
            color: #ffffff; 
            text-transform: uppercase; /* Преобразование текста заголовка в верхний регистр */ 
            font-weight: 700; /* Жирный шрифт для заголовков таблицы */ 
        } 

        tr:hover { 
            background-color: #b2ebf2; /* Цвет при наведении на строку */ 
        } 

        .btn { 
            display: inline-block; 
            background: #00838f; /* Яркий цвет фона кнопки */ 
            color: #fff; 
            padding: 1rem 1.5rem; 
            text-decoration: none; 
            border-radius: 5px; /* Закругленные углы кнопки */ 
            margin: 10px; /* Отступы между кнопками */ 
            transition: background 0.3s, transform 0.2s; /* Плавный переход цвета и эффекта наведения */ 
            font-weight: 700; /* Жирный шрифт для кнопок */ 
        } 

        .btn:hover { 
            background: #005662; /* Темный цвет при наведении */ 
            transform: scale(1.05); /* Немного увеличиваем кнопку при наведении */ 
        } 

        .footer { 
            margin-top: 20px; 
            font-size: 0.9em; 
            color: #555; 
        } 

        /* Добавление стилей для сообщений об ошибках */ 
        .error { 
            color: red; 
            font-weight: bold; 
            margin-top: 20px; 
        } 
    </style> 

    </head>
    <body>
                <?php

                    $username = "Not found"; //по умолчанию имени нет, но как только страница запуститься, имя будет сразу
		    $check_admin = false;

                    if(isset($_GET["username"])){ //принимаем имя с предыдущей страницы через get запрос
                        $username = $_GET["username"]; //запоминаем имя
                    }
                    $IP_V4 = "http://192.168.0.161";
                    $serv = "localhost"; //Нужно будет поменять на сервер Георгия, либо оставить, если запускаем с его ноута
                    $root = "root"; 
                    $password = "";//пароль Георгия
                    $database = "DB_SEEKSHELP";//datafuckinbase

                    $conn = new mysqli($serv, $root, $password, $database); //соединение с базой данных

                    if($conn->connect_error){ //отслеживаем ошибку
                        die("Ошибка: " . $conn->connect_error);
                    }

                    $sql = "SELECT username, rating FROM offers_help ORDER BY rating DESC"; //выбираем имена и рейтинги челов
                    if($result = $conn->query($sql)){
                        $rowsCount = $result->num_rows; //количество полученых из базы данных строк

                        echo "<h2>Текущий рейтинг</h2>";
                        echo "<table>";
                        echo "<thead>";
                        echo "<tr><th>Имя пользователя</th> <th>Общий рейтинг</th></tr>";
                        echo "</thead>";
                        echo "<tbody>";

                        $cnt = 0; //Чтобы вывести только первые значения из таблицы, сделаем счётчик

                        foreach($result as $row){ //перебираем данные из таблицы
                            $cnt++; //каждую интерацию увеличиваем cчётчик
                            echo "<tr>"; 
                                echo "<td>" . $row["username"] . "</td>"; //выводим рейтинг и имя пользователя
                                echo "<td>" . $row["rating"] . "</td>";
                            echo "</tr>";
                            if($cnt >= 10){ //когда вывели первые 10 выходим
                                break;
                            }
                        }

                        $result->free(); //освобождаем память

                    }
                    else{
                        echo "Ошибка: " . $conn->error; //отслеживаем ошибку
                    }

		    $sql0 = "SELECT username FROM admins"; //выбираем имена и рейтинги челов
                    if($result = $conn->query($sql0)){
                        $rowsCount = $result->num_rows; //количество полученых из базы данных строк

                        foreach($result as $row){ //перебираем данные из таблицы
                            if($username == $row["username"]){
                                $check_admin = true;
                                break;
                            }
                        }

                        $result->free(); //освобождаем память

                    }
                    else{
                        echo "Ошибка: " . $conn->error; //отслеживаем ошибку
                    }
                    echo "</tbody>";
                    echo "</table>";

                    echo "<h3>Ваш текущий рейтинг</h3>";

                    $sql1 = "SELECT rating FROM offers_help WHERE username = '$username'"; //Выводим рейтинг нашего чела
                    if($result = $conn->query($sql1)){
                        $rowsCount = $result->num_rows; //количество полученых из базы данных строк

                        foreach($result as $row){
                                echo "<p>" . $row["rating"] . "</p>"; //выводим рейтинг
                        }

                        $result->free(); //освобождаем память
                    }

                    echo "<h3>Ваши текущие баллы</h3>";

                    $sql2 = "SELECT points FROM site WHERE username = '$username'"; //Выводим рейтинг нашего чела
                    if($result = $conn->query($sql2)){
                        $rowsCount = $result->num_rows; //количество полученых из базы данных строк

                        foreach($result as $row){
                                echo "<p>" . $row["points"] . "</p>"; //выводим рейтинг
                        }

                        $result->free(); //освобождаем память
                    }

                    echo "<a href='$IP_V4/bot_project/shop.php?username=$username' class='btn'>Посмотрим, на что вы можете обменять свои баллы!</a>";
		    $conn->close(); //закрываем соединение

		    if($check_admin){
			echo "<h3>Добавить нового админа. Укажите имя пользователя телеграмма, которого хотите назначить админом</h3>";
                        echo "<form>";
                            echo "<p><input type='text' name='new_admin' placeholder='Введите имя пользователя'/></p>";
                            echo "<p><button type='submit' formmethod='get' formaction='$IP_V4/bot_project/addadmin.php'>Добавить админа</button></p>";
                        echo "</form>";
                    }
		    
		    if($check_admin){
			echo "<h3>Изменить рейтинг участников. Укажите имя пользователя, рейтинг которого хотите изменить</h3>";
			echo "<form>";
                            echo "<p><input type='text' name='rat_change' placeholder='Введите имя пользователя'/></p>";
			    echo "<p><input type='text' name='new_rat' placeholder='Введите новый ретинг'/></p>";
                            echo "<p><button type='submit' formmethod='get' formaction='$IP_V4/bot_project/addadmin.php'>Изменить рейтинг</button></p>";
                        echo "</form>";
		    }
		    $check_admin = false;
                ?>
    </body>
</html>